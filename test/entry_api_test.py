import unittest,json 

class TestApp(unittest.TestCase):
     def Variables(self):
         self.api_route = '/mydiary/api/v1/entries'
         self.api_route_2 = '/mydiary/api/v1/entries/1'
         self.entry = {
                            "id":1,
                            'title':"airport",
                            'content':'i love travelling and adventure',
                            "date":'5-8-2018'
            }
         Entry().save(self.entry)
# TEST FOR GETTING ALL ENTRIES
     def test_get_all_entries(self):
            # self.api_route = '/my_diary/api/v1/entries'
         response = self.tester.get(self.api_route)
         self.assertEqual(response.status_code, 200)
         self.assertIn("All Entries", str(response.data))
         self.assertIn('application/json', str(response.headers))
# TEST FOR GETTING SPECIFIC ENTRY BY ID
     def test_get_entry_by_id(self):
            # self.api_route_2= '/my_diary/api/v1/entries/1'
        response = self.tester.get(self.api_route_2)
        self.assertEqual(response.status_code, 200)
        


if __name__ == "__main__":
    unittest.main()