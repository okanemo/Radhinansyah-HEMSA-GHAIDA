#aaaabcccaaa --> 4ab3c3a

def trans(word):
    out = "" #string output
    sum = 0 #container untuk menghitung jumlah huruf bersebelahan yang sama

    for i in range (len(word)):  
        check_letter = word[i]

        if i != len(word)-1 and check_letter == word[i+1]: #jika huruf yang sedang dicek sama dengan huruf disebelah kanannya dan bukan huruf terakhir
            sum += 1 

        else:
            sum += 1 #jika tidak sama sum langsung ditambah 1 terlebih dahulu
            if sum == 1:
                out += check_letter

            else:
                out = out + str(sum) + check_letter
            sum = 0 #reset sum dari 0

    return out

print(trans("aaaabcccaaa"))
        