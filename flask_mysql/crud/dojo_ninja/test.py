from  flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

if __name__ == "__main__":

    ninjas = Ninja.get_ninjas_by_dojo({"dojo_id":1})
    for n in ninjas:
        print(n.first_name, "", n.last_name," dojo id", n.dojo_id)
    
    dojo = Dojo.get_dojo_by_id(1)
    print(dojo.name)
