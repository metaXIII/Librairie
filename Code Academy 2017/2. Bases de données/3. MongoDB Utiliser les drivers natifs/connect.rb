#!/usr/bin/env ruby

require "rubygems"
require "mongo"
include Mongo

$client = Mongo::Client.new(['127.0.0.1:27017'], :database => 'LXF')
Mongo::Logger.logger.level = ::Logger::ERROR
$collection = $client[:someData]
puts 'Connected with version:' 
puts Mongo::VERSION

# Insertion en base de données
500.times do |n|
  doc = {
    :username => "Linux Format",
    :code => rand(4),
    :time => Time.now.utc,
    :n => n*n
  }
  $collection.insert_one(doc)
end





$collection.find({"n" => {"$gt" => 205000}, "code" => {"$lt" => 1}}).each do |doc|
  puts doc
end


puts "Mettre à jour des docs"
$result = $collection.find({"n" => {"gt" => 205000}}).update_many({"$inc" => {:code => 10}})
puts $result.n

puts "Liste des index"
$collection.indexes.each do |index|
  p index
end


# Insertions d'un nouvel utilisateur
$client.database.users.create(
  username: 'linuxFormat',
  password: 'aPass',
  roles: [Mongo::Auth::Roles::READ_WRITE]
)

$result = $collection
