def product_of_multiples(factor, limit):
    product = 1
    for i in range(factor, limit, factor):
        product *= i
    return product
print(product_of_multiples(3, 25))