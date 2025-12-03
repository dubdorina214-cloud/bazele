#число буквами
number=int(input("введите трехзначное число:"))
if number<100 or number>999:print("введите трехзначное число!")
else:
    hundreds=number//100
    tens=(number//10)%10
    ones=number%10
    text=""
    match hundreds:
                 
                case 1:text+="сто"
                case 2:text+="двести"
                case 3:text+="триста"
                case 4:text+="четыреста"
                case 5:text+="пятьсот"
                case 6:text+="шестьсот"
                case 7:text+="семьсот"
                case 8:text+="восомьсот"
                case 9:text+="девятьсот"
    if (tens==1):
        match ones:
              case 0:text+="десять"
              case 1:text+="одинадцать"
              case 2:text+="двенадцать"
              case 3:text+="тренадцать"
              case 4:text+="цетырнадцать"
              case 5:text+="пятнадцать"
              case 6:text+="шестнадцать"
              case 7:text+="семнадцать"
              case 8:text+="восемнадцать"
              case 9:text+="девятнадцать"
     
    else:
        match tens:
            case 2:text+= " двадцать"
            case 3:text+= " тридцать"
            case 4:text+= " сорок"
            case 5:text+= " пятьдесят"
            case 6:text+= " шустьдесят"
            case 7:text+= " семьдесят"
            case 8:text+=  " восемьдесят"
            case 9:text+=  " девяносто"
      
        match ones:
            case 1:text+=  " один"
            case 2:text+= " два"
            case 3:text+= " три"
            case 4:text+= " четыре"
            case 5:text+= " пять"
            case 6:text+= " шесть"
            case 7:text+=  " семь"
            case 8:text+= " восемь" 
            case 9:text+= " девять"
    print(text.strip())
