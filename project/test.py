import jinja2
location=['beijing','shanghai','guangzhou','shenzhen']
{% for each in location %}
i am living in {{ each }}
{% endfor %}



'''location=['beijing','shanghai','guangzhou','shenzhen']
for each in location:
    print("i am living in "+each)'''


'''xiaoming=1
while xiaoming < 18:
    print('Xiaoming age is'+str(xiaoming))
    print("Xiaoming can't drink alcoho")
    xiaoming += 1'''

'''location={'beijing':'010','shanghai':'021','guangzhou':'022','shenzhen':'0755'}
for each,munber in location.items():
    print(each+'******'+munber)'''