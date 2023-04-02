from lxml import etree

tree = etree.parse('xpath_course.html')
print(tree)
# list1=tree.xpath('//body//ul//li')
# print(f'{list1}+{len(list1)}')
# list2=tree.xpath('//ul/li[@id="1"]/text()')
# print(list2)
# list3=tree.xpath('//ul/li[@id="4"]/@class')
# print(list3)
# list4=tree.xpath('//ul/li[contains(@id,"l")]/text()')
# print(list4)
list5=tree.xpath('//ul/li[@id="a2" and @class="2c"]/text()')
print(list5)