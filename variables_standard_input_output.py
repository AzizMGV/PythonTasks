Катя узнала, что ей для сна надо XX минут. В отличие от Коли, Катя ложится спать после полуночи в HH часов и MM минут. Помогите Кате определить, на какое время ей поставить будильник, чтобы он прозвенел ровно через XX минут после того, как она ляжет спать.

На стандартный ввод, каждое в своей строке, подаются значения XX, HH и MM. Гарантируется, что Катя должна проснуться в тот же день, что и заснуть. Программа должна выводить время, на которое нужно поставить будильник: в первой строке часы, во второй — минуты.

X = int(input()) #Ввод количество минут, необходимых Кате для сна
H = int(input()) #Ввод часы. Время, когда она ложиться спать.
M = int(input()) #Ввод минуты. Время, когда она ложиться спать.
hours = ((H*60)+X+M)//60   #Умножаем часы на 60, чтобы перевести в минуты, затем прибавляем сколько минут ей надо спать + минуты, когда она ложиться спать. Получившееся число делим на цело на 60, чтобы перевести минуты в часы
minutes = (X+M)%60  #Складываем минуты, необходимые Кате для сна с минутами, когда она ложиться и берем остаток от деления
print(hours) #Выводить время, на которое нужно поставить будильник: часы
print(minutes) #Выводить время, на которое нужно поставить будильник: минуты
