# Just learning ruby. question is trivial
t = gets.to_i

i = 0
while i < t do
    inputs = gets.chomp
    input = inputs.split()
    quantity = input[0].to_i
    price = input[1].to_i
    expense = quantity*price.to_f
    if quantity > 1000
        expense = 0.9*expense
    end
    i += 1
    puts format("%.6f", expense)
end