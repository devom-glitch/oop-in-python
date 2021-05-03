class Movie:
    def __init__(self,movie_id,movie_name,ticket_cost):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.ticket_cost = ticket_cost
        self.category = "Default"

    def price_category(self):
        if(0<self.ticket_cost and self.ticket_cost<150):
            self.category = "General"
        elif(150<=self.ticket_cost and self.ticket_cost<250):
            self.category = "Silver"
        elif(250<=self.ticket_cost and self.ticket_cost<350):
            self.category = "Gold"
        else:
            self.category = "Platinum"
    
class Movie_Ticket:
    def __init__(self,customer_name,movie_name,viewerCount,totalTicketCost):
        self.customer_name = customer_name
        self.movie_name = movie_name
        self.viewerCount = viewerCount
        self.totalTicketCost = totalTicketCost


def getCategoryWiseCount(movies):
    category_count = {}
    for movie in movies:
        movie.price_category()
        if(category_count.get(movie.category,0)):
            category_count[movie.category] += 1
        else:
            category_count[movie.category] = 1
    return category_count

def bookMovieTicket(movies,customer_name,movie_name,viewer_count):
    totalticketcost = 0
    for movie in movies:
        if movie.movie_name == movie_name:
            totalticketcost = movie.ticket_cost * viewer_count
            return Movie_Ticket(customer_name,movie_name,viewer_count,totalticketcost)
    return None

if __name__ == '__main__':
    numberMovie = int(input())
    movies = []
    for _ in range(numberMovie):
        movies.append(Movie(int(input()),input(),int(input())))
    category_count = getCategoryWiseCount(movies)
    bookedTicket = bookMovieTicket(movies,input(),input(),int(input()))
    print("Category wise ticket count:")
    for k,v in category_count.items():
        print(f'{k}:{v}')
    print(f'{bookedTicket.customer_name} {bookedTicket.totalTicketCost}')        
            
#         Copyright (C) 1989, 1991-2019 Free Software Foundation.

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see http://www.gnu.org/licenses/.
