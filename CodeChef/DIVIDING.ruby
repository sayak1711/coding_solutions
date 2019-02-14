n = gets.to_i
stampsinp = gets.chomp
stamps = stampsinp.split()
sum = 0
for i in 0..n-1 do
    item = stamps.at(i).to_i
    sum += item
end
if sum == (n*(n+1))/2
    puts "YES"
else
    puts "NO"
end
