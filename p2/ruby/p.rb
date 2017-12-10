#!/usr/bin/ruby

def fib()
	a = 1; b = 2; tmp = 0, sum = 0
	((a%2 == 0) ? (sum+=a) : (); (tmp = a + b; a = b; b = tmp)) while a < Integer(ARGV[0])
	sum
end

puts(fib())

