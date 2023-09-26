class Project:
    def __init__(self, name, language, description, added_element):
        self._name = name
        self._language = language
        self._description = description
        self._added_element = added_element

    def get_name(self):
        """
        gets the name of the Project object
        :return: String (the name of the project)
        """
        return self._name

    def get_language(self):
        """
        gets the programming language used for the Project object
        :return: String (name of the language)
        """
        return self._language

    def get_description(self):
        """
        gets the brief description of the Project object
        :return: String (brief description)
        """
        return self._description

    def get_added_element(self):
        """
        gets the feature/element/option that the coder implemented for learning purposes
        Example: If a new coder has never imported from the Python library before, then
            they could use that in this project to gain experience.
        :return: String (added element)
        """
        return self._added_element

    def write_to_text_file(self):
        """
        Writes the details of the Project to a text file
        :return: Bool (True when successfully written)
        """
        with open("project_info.txt", "a") as f:
            f.write(self.get_name())
            f.write("\nLanguage: " + self.get_language() + "\n")
            f.write("Description: " + self.get_description() + "\n")
            f.write("Challenge Element: " + self.get_added_element() + "\n\n")
            f.close()
            return True


class ProjectTracker:
    def __init__(self, name, user):
        self._name = name
        self._user = user
        self._track_hash = {}

    def get_name(self):
        """
        gets the user created name of the Project Tracker
        :return: String (project tracker name)
        """
        return self._name

    def get_user(self):
        """
        gets the name of the user that controls the Project Tracker
        :return: String (user name)
        """
        return self._user

    def add_project(self, project_name, project_object):
        """
        adds a project to the track_hash dictionary, with the name of the project as key, and the project
            object as the value
        :return: Bool (True when it is successfully added, False otherwise)
        """
        if project_name not in self._track_hash:
            self._track_hash[project_name] = project_object
            return True

        else:
            return False

    def print_project_list(self):
        """
        Prints the keys of the project list and the language in parentheses
        :return: None
        """
        for key in self._track_hash:
            print(key + " (" + self._track_hash[key].get_language() + ")")

    def print_specific_language_list(self, language):
        """
        Prints all the projects using the specified language in the Project Tracker
        :param language: String (programming language)
        :return: None
        """
        print("All projects in " + self.get_name() + " using " + language + ":")
        for key in self._track_hash:
            if self._track_hash[key].get_language().upper() == language.upper():
                print(key)









Joes_Tracker = ProjectTracker("Joe's Tracker", "Joe")

hello_world = Project("Hello World", "Python", "Prints Hello World", "Print Statement")
dino_collect = Project("Dinosaur Toy Collection", "C#", "Keeps Track of User Dino Toy Collection", "Arrays")

Joes_Tracker.add_project(hello_world.get_name(), hello_world)
Joes_Tracker.add_project(dino_collect.get_name(), dino_collect)

Joes_Tracker.print_specific_language_list("C#")

Joes_Tracker.write_to_text_file(dino_collect)
Joes_Tracker.write_to_text_file(hello_world)







