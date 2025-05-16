def SaveUpdatedData(self):
    #     try:
    #         connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
    #         curs = connection.cursor()
    #         # Replace the below with actual field values from your entry widgets
    #         name = self.entry_name.get()
    #         email = self.entry_email.get()
    #         contact = self.entry_contact.get()
    #         address = self.entry_address.get()
            
    #         curs.execute("""
    #             UPDATE contact_register 
    #             SET name=%s, email=%s, address=%s 
    #             WHERE contact=%s
    #         """, (name, email, address, contact))
            
    #         connection.commit()
    #         connection.close()
    #         messagebox.showinfo("Success", "Record updated successfully!")
    #         self.DisplayData()  # Refresh table
    #     except Exception as e:
    #         messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)