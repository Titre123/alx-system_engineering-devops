#!/usr/bin/env ruby
#regex matches school

puts ARGV[0].scan(/S[\w]+l/).join
