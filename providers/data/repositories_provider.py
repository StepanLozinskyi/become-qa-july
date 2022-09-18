class RepositoriesProvider:

    @staticmethod
    def existing_repository():
        return{
            'name': 'become-qa-auto',
            'total_count': 1
        }

    @staticmethod
    def non_existing_repository():
        return{
            'name': 'ewtwetertefetrt4342ewr',
            'total_count': 0
        }