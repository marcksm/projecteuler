#!/usr/bin/ruby

def nextprime(n)
	while TRUE
		n+=1;i=2
		((n%i == 0) ? (break):(); i+=1) while i <= n
		if i == n
			return n
		end
	end
end

def run(n)
	p = 2; total = 1; bp = 2
	while total < n
		if n%p == 0
			
			total *= p
			bp = p
		end
		if (p > n) 
			return bp
		end
		p = nextprime(p)
	end
	return bp
end


puts(run(Integer(ARGV[0])))
