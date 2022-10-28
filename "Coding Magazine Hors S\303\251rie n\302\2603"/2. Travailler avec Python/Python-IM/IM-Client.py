#!/usr/bin/env python2
# coding: utf8

import threading
import gtk
import gobject
import socket
import re
import time
import datetime

gobject.threads_init()


class MainWindow(gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.set_title("IM Client")
        vbox = gtk.VBox()
        hbox = gtk.HBox()
        self.username_label = gtk.Label()
        self.text_entry = gtk.Entry()
        send_button = gtk.Button("Send")
        self.text_buffer = gtk.TextBuffer()
        text_view = gtk.TextView(self.text_buffer)
        self.connect("destroy", self.graceful_quit)
        send_button.connect("clicked", self.send_message)
        self.text_entry.connect("activate", self.send_message)
        vbox.pack_start(text_view)
        hbox.pack_start(self.username_label, expand=False)
        hbox.pack_start(self.text_entry)
        hbox.pack_end(send_button, expand=False)
        vbox.pack_end(hbox, expand=False)
        self.add(vbox)
        self.show_all()
        self.configure()

    def ask_for_info(self, question):
        dialog = gtk.MessageDialog(parent=self, type=gtk.MESSAGE_QUESTION,
                                   flags=gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                                   buttons=gtk.BUTTONS_OK_CANCEL, message_format=question)
        entry = gtk.Entry()
        entry.show()
        dialog.vbox.pack_end(entry)
        response = dialog.run()
        response_text = entry.get_text()
        dialog.destroy()
        if response == gtk.RESPONSE_OK:
            return response_text
        else:
            return None

    def configure(self):
        server = self.ask_for_info("server_adress:port")
        regex = re.search('^(\d+\.\d+\.\d+\.\d+):(\d+)$', server)
        address = regex.group(1).strip()
        port = regex.group(2).strip()
        self.username = self.ask_for_info("username")
        self.username_label.set_text(self.username)
        self.network = Networking(self, self.username, address, int(port))
        self.network.listen()

    def add_text(self, new_text):
        text_with_timestamp = "{0}{1}".format(datetime.datetime.now(), new_text)
        end_itr = self.text_buffer.get_end_itr()
        self.text_buffer.insert(end_itr, text_with_timestamp)

    def send_message(self, widget):
        new_text = self.text_entry.get_text()
        self.text_entry.set_text("")
        message = "{0} says: {1}\n".format(self.username, new_text)
        self.network.send(message)

    def graceful_quit(self, widget):
        gtk.main_quit()
        self.network.send("QUIT")
        self.network.tidy_up()


class Networking():
    def __init__(self, window, username, server, port):
        self.window = window
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((server, port))
        self.listening = True
        self.send("USERNAME {0}".format(username))

    def listener(self):
        while self.listening:
            data = ""
            try:
                data = self.socket.recv(1024)
            except socket.error:
                "Unable to receive data"
            self.handle_msg(data)
            time.sleep(0.1)

    def listen(self):
        self.listen_thread = threading.Thread(target=self.listener)
        self.listen_thread.daemon = True
        self.listen_thread.start()

    def send(self, message):
        print "Sending: {0}".format(message)
        try:
            self.socket.sendall(message)
        except socket.error:
            print "Unable to send message"

    def tidy_up(self):
        self.listening = False
        self.socket.close()
        gobject.idle_add(self.window.add_text, "Server has quit\n")

    def handle_msg(self, data):
        if data == "QUIT":
            self.tidy_up()
        elif data == "":
            self.tidy_up()
        else:
            gobject.idle_add(self.window.add_text, data)

if __name__ == '__main__':
    MainWindow()
    gtk.main()