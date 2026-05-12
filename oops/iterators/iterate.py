list1=[1,2,3,4,5]

it=iter(list1)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


# creating a custom iterator

class EvenNumbers:

    def __iter__(self):
        self.n=2
        return self

    def __next__(self):
        x=self.n
        self.n+=2
        return x



e1=EvenNumbers()
p1=iter(e1)

print(next(p1))
print(next(p1))
print(next(p1))
