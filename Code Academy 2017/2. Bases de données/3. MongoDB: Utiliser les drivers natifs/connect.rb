#!/usr/bin/env ruby

require "rubygems"
require "mongo"
include Mongo

$client = Mongo::Client.new(['127.0.0.1:27017'], :database => 'LXF')
Mongo::Logger.logger.level = ::Logger::ERROR
$collection = $client[:someData]
puts 'Connected with version:' 
puts Mongo::VERSION