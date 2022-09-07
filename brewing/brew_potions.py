from brewing import potion_class
from brewing import containers
from brewing import cooking
from brewing import inspection
from brewing.ingredients import fish_eyes, unicorn_hair, tea_leaves


def make_example_potion(student_name):
    my_potion = potion_class.Potion(student_name=student_name)
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=containers.old_kettle, heat_source=cooking.eternal_flame)
    # Simmer for 5 hours.
    cooking.simmer(my_potion, duration=5)
    print("You have successfully run make_example_potion, well done :).")
    return my_potion


def make_python_expert_potion(student_name: str) -> potion_class.Potion:
    """Cook an expert potion.
    
    Set up a pewter cauldron and light a fire underneath it.
    Add fish eyes, unicorn hair and tea leaves.
    Let simmer for 2 hours.

    Parameters
    ----------
    student_name : str 
        The name of the cook.

    Returns
    -------
    expert_potion : class object
        The cooked expert posion.
    """
    print("I am a Python Expert")
    expert_potion = potion_class.Potion(student_name=student_name)
    expert_potion.setup(container=containers.pewter_cauldron, heat_source=cooking.fire)
    expert_potion.add_ingredients([fish_eyes, unicorn_hair, tea_leaves])
    cooking.simmer(expert_potion, duration=2)
    return expert_potion


if __name__ == "__main__":
    my_name = 'ASPP student'
    my_potion = make_python_expert_potion(student_name=my_name)
    # Let Snape inspect the potion
    inspection.inspection_by_Snape(potion=my_potion, target_potion='python_expert')
