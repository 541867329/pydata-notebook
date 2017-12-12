import mydemo.randomData.UtilrandomData as randomData
import random

layer5path = '/home/yjhl/PycharmProjects/pydata-notebook/mydemo/randomData/layer5'
with open(layer5path) as file:
    data = file.read()
codelist = data.split('\n')
# print(codelist)
for i in range(0, 1):
    for i in range(0, 100000):
        ind = int(random.randint(0, len(codelist)-1))
        region = codelist[ind].split('\t')
        address = region[4]+region[3]+region[2]+region[1]+str(random.randint(1, 10))+'号楼'
        regioncode = region[0]
        person = randomData.getData()
        a = '''insert into person (person_id,name,sex,idnt_cert_num,link_tel,birth_date,residence,residence_code,belong_org_id) values (replace(UUID(),'-',''),''' \
            + '|' + str(person[1]) + '|' \
            + ',|' + str(person[5]) + '|' \
            + ',|' + str(person[0]) + '|' \
            + ',|' + str(person[2]) + '|' \
            + ',|' + str(person[3]) + '|' \
            + ',|' + str(address) + '|' \
            + ',|' + str(regioncode) + '|' \
            + ',|' + 'e6bfb30d0d01442aa3462eff5dc2bd38' + '|' \
            + ');'
        b=a.replace('|', '\'')+'\n'
        file = open('/home/yjhl/Desktop/person.sql', 'a')
        file.write(b)
        file.close()
