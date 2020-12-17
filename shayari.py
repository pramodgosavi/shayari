
oscillation = [' थिरकते ',' सिमटते ',' झुलसते ']
facial= [' नज़रों ',' होठों ',' नैनों ',' गालों ',' माथें ']
natural=[' बूँद ',' ओस ', ' बारीश ',' हवा ']
bathroom=[' फ़िसलना ',' गिरना ',' टपकना ',' उलझना ',' सुलझना ',' निकलना ',' सवरना ']
emotion=[' याद ',' डराता ',' हसाता ',' रुलाता ']
movement=[' दूर जाना ',' पास आना ', ' रौशनी फैलाना ',' गुम हो जाना']
f=open("shayari.doc","w")
count=1
for i in oscillation:
    for j in facial:
        for k in natural:
            for l in bathroom:
                for m in emotion:
                    for n in movement:
                        f.write(str(count) + ")\n "+i +' हुए '+ j +' से '+ k +' का '+ l +'|'+ '\n' + m + ' है मुझे तेरा वही '+ n +'||' + '\n\n')
                        count=count+1

f.close()


