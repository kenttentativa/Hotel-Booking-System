from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Room, Booking
from .forms import RoomForm, BookingForm

# Home Page
def home(request):
    return render(request, 'home.html')

# View all rooms
@login_required
def view_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/view_rooms.html', {'rooms': rooms})

# Add a new room
@login_required
def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Ensure 'dashboard' exists in urls.py
    else:
        form = RoomForm()
    return render(request, 'rooms/add_room.html', {'form': form})

# Delete a room
@login_required
def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    room.delete()
    messages.success(request, "Room deleted successfully!")
    return redirect('view_rooms')

@login_required
def edit_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('view_rooms')  # Redirect back to the room list
    else:
        form = RoomForm(instance=room)
    
    return render(request, 'rooms/edit_room.html', {'form': form, 'room': room})

# View all bookings
@login_required
def view_bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/view_bookings.html', {'bookings': bookings})

# Add a new booking
@login_required
def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking added successfully!")
            return redirect('home')  # Redirect to home after adding a booking
    else:
        form = BookingForm()
    return render(request, 'bookings/add_booking.html', {'form': form})



# Delete a booking
@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    messages.success(request, "Booking deleted successfully!")
    return redirect('view_bookings')

@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('view_bookings')  # Redirect after saving

    else:
        form = BookingForm(instance=booking)

    return render(request, 'bookings/edit_booking.html', {'form': form, 'booking': booking})

# Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'accounts/login.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')
