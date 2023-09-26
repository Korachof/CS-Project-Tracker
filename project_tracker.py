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

