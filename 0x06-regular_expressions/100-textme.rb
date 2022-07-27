#!/usr/bin/env ruby
puts.ARGS[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(",")
