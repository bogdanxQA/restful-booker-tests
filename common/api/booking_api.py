class BookingAPI:

    def __init__(self, client):
        self.client = client
        

    def get_full_list_booking(self):
        res = self.client.get(endpoint='/booking/')
        return res
    
    def get_booking_by_id(self, booking_id):
        res = self.client.get(endpoint=f'/booking/{booking_id}')
        return res
    
    def create_booking(self, booking_data):
        res = self.client.post(endpoint='/booking/', json = booking_data)
        return res
    
    def full_update_booking(self, booking_data, booking_id, cookies):
        res = self.client.put(endpoint=f'/booking/{booking_id}', json = booking_data, cookies = cookies)
        return res
    
    def partial_update_booking(self, booking_data, booking_id, cookies):
        res = self.client.patch(endpoint=f'/booking/{booking_id}', json = booking_data, cookies = cookies)
        return res
    
    def delete_booking(self, booking_id, cookies):
        res = self.client.delete(endpoint=f'/booking/{booking_id}', cookies = cookies)
        return res


    