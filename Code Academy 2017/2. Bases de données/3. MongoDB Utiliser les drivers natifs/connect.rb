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
# 500.times do |n|
#   doc = {
#     :username => "Linux Format",
#     :code => rand(4),
#     :time => Time.now.utc,
#     :n => n*n
#   }
#   $collection.insert_one(doc)
# end



$collection.find({"n" => {"$gt" => 205000}, "code" => {"$lt" => 1}}).each do |doc|
  puts doc
end
