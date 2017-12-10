#!/usr/bin/ruby

def allnatural ()
	sum = 0; i = 1
	(i%3 == 0 or i%5 == 0) ? (sum+=i; i+=1) : (i+=1) while i <= 999
	sum
end
puts(allnatural())
