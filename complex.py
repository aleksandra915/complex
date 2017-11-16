#!/usr/local/bin/python

class Complex(object):
	def __init__(self, real, imag=0.0):
		self.real = real
		self.imag = imag

	def __add__(self, other):
		return Complex(self.real + other.real, self.imag + other.imag)
	
	def __sub__(self, other):
	        return Complex(self.real - other.real,
        	               self.imag - other.imag)

	def __mul__(self, other):
		return Complex(self.real*other.real - self.imag*other.imag,
               			 self.imag*other.real + self.real*other.imag)

	def __truediv__(self, other):
        	r = float(other.real**2 + other.imag**2)
        	return Complex((self.real*other.real+self.imag*other.imag)/r, (self.imag*other.real-self.real*other.imag)/r)

	def __abs__(self):
        	return sqrt(self.real**2 + self.imag**2)

	def __neg__(self):   # defines -c (c is Complex)
        	return Complex(-self.real, -self.imag)

	def __eq__(self, other):
        	return self.real == other.real and self.imag == other.imag


	def __str__(self):
        	return '(%g, %g)' % (self.real, self.imag)

a = Complex(1,2)
b = Complex(-5,-3)
c = Complex(1,-5)
d = Complex(-3,-4)

