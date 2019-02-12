t = gets.to_i

i = 0
while i < t do
    g = gets.to_i
    j = 1
    while j <= g do
        inp = gets.chomp
        inps = inp.split()
        i = inps[0].to_i  # 1 means all head 2 tail
        n = inps[1].to_i # number of rounds
        q = inps[2].to_i # 1 head 2 tail

        if q == 1
            if i == 1
                puts (n/2)
            else
                if n % 2 == 0
                    puts (n/2)
                else
                    puts n-(n/2)
                end
            end
        else
            if i == 1
                if n % 2 == 0
                    puts (n/2)
                else
                    puts n-(n/2)
                end
            else
                puts (n/2)
            end
        end
        j += 1
    end
    i += 1
end