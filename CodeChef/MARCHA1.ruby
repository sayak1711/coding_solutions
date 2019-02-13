def SubsetSum(arr, sum, n)
    if sum == 0
        return true
    elsif n == 0 and sum != 0
        return false
    elsif arr[n-1] > sum
        return SubsetSum(arr, sum, n-1)
    end
    return SubsetSum(arr, sum-arr[n-1], n-1) || SubsetSum(arr, sum, n-1)
end

number_of_test_cases = gets.to_i

for testcase in 1..number_of_test_cases do
    inputs = gets.chomp
    input_list = inputs.split()
    number_of_bank_notes = input_list[0].to_i
    muggers_demand = input_list[1].to_i
    notes = []
    for k in 0..number_of_bank_notes-1 do
        notes.push(gets.to_i)
    end
    if SubsetSum(notes, muggers_demand, number_of_bank_notes)
        puts "Yes"
    else
        puts "No"
    end
end