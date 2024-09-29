from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import requests
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, Movie, Rating
from .validators import validate_user_password


from random import randint
from movie_recommender.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from django.core.mail import send_mail
def send_otp(email):
    subject = 'OTP for Movie Recommendation'
    otp = randint(100000, 999999)
    message = f"Greetings!\nYour OTP is {otp}\n\nThank You!"
    from_email = EMAIL_HOST_USER
    print(EMAIL_HOST_USER)
    print(EMAIL_HOST_PASSWORD)
    to_list = [email]
    send_mail(subject, message, from_email, to_list)
    return otp


def update(movie, profile, upd1, upd2):
    print(upd1,upd2)
    movie_dict = movie.__dict__
    movie_info = list(movie_dict.keys())[3:] # Update index if model update

    for key in movie_info:
        if movie_dict[key] == True:
            genre = profile.__dict__[key]
            ratings, movies = genre.split()
            ratings, movies = float(ratings) + upd1, int(movies) + upd2
            profile.__dict__[key] = str(ratings) + ' ' + str(movies)
    
    profile.save()


def Register(request):
    if request.method == 'POST':
        if 'username' in request.POST:
            username = request.POST['username']
            email = request.POST['signup-email']
            password = request.POST['signup-password']
            confirm_password = request.POST['confirm-signup-password']
            
            if User.objects.filter(username=username).exists():
                messages.error(request, "Email already registered!!!")
                return render(request, 'main/register.html')
            
            if(password!=confirm_password):
                messages.error(request, 'Password do not match!!!')
                return render(request, 'main/register.html')
            
            try:
                validate_user_password(password)
            except ValidationError as e:
                messages.error(request, e.message_dict['password'][0])
                return render(request, 'main/register.html')

            otp = send_otp(email)
            request.session['otp'] = otp
            request.session['email'] = email
            request.session['password'] = password
            request.session['username'] = username
            messages.success(request, "OTP has been sent to your email address!!")
            return render(request, 'main/otp.html')
        
        if('otp' in request.POST):
            if(int(request.POST['otp'])==int(request.session['otp'])):
                username = request.session['username']
                email = request.session['email']
                password = request.session['password']
                User.objects.create_user(username=username, email=email, password=password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('main:Form')
            else:
                messages.error(request, "Invalid OTP!!!")
                return render(request, 'main/otp.html')
            
    return render(request, 'main/register.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['signin-password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            next = request.GET.get('next')
            
            try:
                profile = Profile.objects.get(user=user)
            except Profile.DoesNotExist:
                return redirect('main:Form')
            
            if next:
                return redirect(next)
            else:
                return redirect('main:Home')
        else:
            messages.error(request, 'Incorrect Username or Password')
            return render(request, 'main/login.html')
    
    return render(request, 'main/login.html')


@login_required
def Form(request):
    user = request.user
    if Profile.objects.filter(user=user).exists():
        return redirect('main:Home')
    
    if request.method == 'POST':
        user = request.user
        Adventure = str(float(request.POST['Adventure'])) + ' 1'
        Animation = str(float(request.POST['Animation'])) + ' 1'
        Children = str(float(request.POST['Children'])) + ' 1'
        Comedy = str(float(request.POST['Comedy'])) + ' 1'
        Fantasy = str(float(request.POST['Fantasy'])) + ' 1'
        Romance = str(float(request.POST['Romance'])) + ' 1'
        Drama = str(float(request.POST['Drama'])) + ' 1'
        Action = str(float(request.POST['Action'])) + ' 1'
        Crime = str(float(request.POST['Crime'])) + ' 1'
        Thriller = str(float(request.POST['Thriller'])) + ' 1'
        Horror = str(float(request.POST['Horror'])) + ' 1'
        Mystery = str(float(request.POST['Mystery'])) + ' 1'
        Sci_Fi = str(float(request.POST['Sci_Fi'])) + ' 1'
        IMAX = str(float(request.POST['IMAX'])) + ' 1'
        Documentary = str(float(request.POST['Documentary'])) + ' 1'
        War = str(float(request.POST['War'])) + ' 1'
        Musical = str(float(request.POST['Musical'])) + ' 1'
        Western = str(float(request.POST['Western'])) + ' 1'
        Film_Noir = str(float(request.POST['Film_Noir'])) + ' 1'
        
        Profile.objects.create(user=user,Adventure=Adventure,Animation=Animation,Children=Children,Comedy=Comedy,Fantasy=Fantasy,Romance=Romance,Drama=Drama,Action=Action,Crime=Crime,Thriller=Thriller,Horror=Horror,Mystery=Mystery,Sci_Fi=Sci_Fi,IMAX=IMAX,Documentary=Documentary,War=War,Musical=Musical,Western=Western,Film_Noir=Film_Noir)

        return redirect('main:Home')
    return render(request, 'main/form.html')


@login_required
def Home(request):
    if 'search_term' in request.GET:
        search = request.GET.get('search_term','')
        results = []
        if search:
            results = list(Movie.objects.filter(title__icontains=search).values('title')[:5])

        return JsonResponse(results, safe=False)

    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        return redirect('main:Form')

    Adventure = profile.Adventure.split()
    Animation = profile.Animation.split()
    Children = profile.Children.split()
    Comedy = profile.Comedy.split()
    Fantasy = profile.Fantasy.split()
    Romance = profile.Romance.split()
    Drama = profile.Drama.split()
    Action = profile.Action.split()
    Crime = profile.Crime.split()
    Thriller = profile.Thriller.split()
    Horror = profile.Horror.split()
    Mystery = profile.Mystery.split()
    Sci_Fi = profile.Sci_Fi.split()
    IMAX = profile.IMAX.split()
    Documentary = profile.Documentary.split()
    War = profile.War.split()
    Musical = profile.Musical.split()
    Western = profile.Western.split()
    Film_Noir = profile.Film_Noir.split()

    user_feat = []
    user_feat.append(float(Adventure[0])/int(Adventure[1]))
    user_feat.append(float(Animation[0])/int(Animation[1]))
    user_feat.append(float(Children[0])/int(Children[1]))
    user_feat.append(float(Comedy[0])/int(Comedy[1]))
    user_feat.append(float(Fantasy[0])/int(Fantasy[1]))
    user_feat.append(float(Romance[0])/int(Romance[1]))
    user_feat.append(float(Drama[0])/int(Drama[1]))
    user_feat.append(float(Action[0])/int(Action[1]))
    user_feat.append(float(Crime[0])/int(Crime[1]))
    user_feat.append(float(Thriller[0])/int(Thriller[1]))
    user_feat.append(float(Horror[0])/int(Horror[1]))
    user_feat.append(float(Mystery[0])/int(Mystery[1]))
    user_feat.append(float(Sci_Fi[0])/int(Sci_Fi[1]))
    user_feat.append(float(IMAX[0])/int(IMAX[1]))
    user_feat.append(float(Documentary[0])/int(Documentary[1]))
    user_feat.append(float(War[0])/int(War[1]))
    user_feat.append(float(Musical[0])/int(Musical[1]))
    user_feat.append(float(Western[0])/int(Western[1]))
    user_feat.append(float(Film_Noir[0])/int(Film_Noir[1]))

    response = requests.post('http://api:80/user/predict', json={'input': user_feat})
    movies = []
    print(response)
    if response.status_code == 200:
        movies = response.json()['movies']

    context = {'similar': movies}
    
    return render(request, 'main/home.html', context=context)


@login_required
def Details(request, title):
    print(title)
    movie = Movie.objects.get(title=title)
    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        if 'clear' in request.POST:
            rating = Rating.objects.get(movie=movie, user=user)
            update(movie, profile, -rating.rating, -1)
            rating.delete()
        else:
            rate = float(request.POST['rating'])
            if 'change' in request.POST:
                rating = Rating.objects.get(movie=movie, user=user)
                update(movie, profile, rate-rating.rating, 0)
                rating.rating = rate
                rating.save()
            elif 'rate' in request.POST:
                update(movie, profile, rate, 1)
                rating = Rating.objects.create(movie=movie, user=user, rating=rate)


    genres = []
    if movie.Adventure:
        genres.append('Adventure')
    if movie.Animation:
        genres.append('Animation')
    if movie.Children:
        genres.append('Children')
    if movie.Comedy:
        genres.append('Comedy')
    if movie.Fantasy:
        genres.append('Fantasy')
    if movie.Romance:
        genres.append('Romance')
    if movie.Drama:
        genres.append('Drama')
    if movie.Action:
        genres.append('Action')
    if movie.Crime:
        genres.append('Crime')
    if movie.Thriller:
        genres.append('Thriller')
    if movie.Horror:
        genres.append('Horror')
    if movie.Mystery:
        genres.append('Mystery')
    if movie.Sci_Fi:
        genres.append('Sci_Fi')
    if movie.IMAX:
        genres.append('IMAX')
    if movie.Documentary:
        genres.append('Documentary')
    if movie.War:
        genres.append('War')
    if movie.Musical:
        genres.append('Musical')
    if movie.Western:
        genres.append('Western')
    if movie.Film_Noir:
        genres.append('Film_Noir')

    context = {'movie': movie, 'genres': genres}

    try:
        context['rating'] = Rating.objects.get(movie=movie, user=user).rating
    except Rating.DoesNotExist:
        pass

    return render(request, 'main/movie.html', context=context)


@login_required
def Similar(request, title):
    movie = Movie.objects.get(title=title)

    movie_feat = []

    if movie.Adventure:
        movie_feat.append(1)
    else:
        movie_feat.append(0)
    if movie.Animation:
        movie_feat.append(1)
    else:
        movie_feat.append(0)
    if movie.Children:
        movie_feat.append(1)
    else:
        movie_feat.append(0)
    if movie.Comedy:
        movie_feat.append(1)
    else:
        movie_feat.append(0)
    if movie.Fantasy:
        movie_feat.append(1)
    else:
        movie_feat.append(0)
    if movie.Romance:
        movie_feat.append(1)
    else:
        movie_feat.append(0)
    if movie.Drama:
        movie_feat.append(1)
    else:
        movie_feat.append(0)
    if movie.Action:
        movie_feat.append(1)
    else:
        movie_feat.append(0)
    if movie.Crime:
        movie_feat.append(1)
    else:
        movie_feat.append(0)
    if movie.Thriller:
        movie_feat.append(1)
    else:
        movie_feat.append(0)
    if movie.Horror:
        movie_feat.append(1)
    else:
        movie_feat.append(0)
    if movie.Mystery:
        movie_feat.append(1)
    else:
        movie_feat.append(0)
    if movie.Sci_Fi:
        movie_feat.append(1)
    else:
        movie_feat.append(0)
    if movie.IMAX:
        movie_feat.append(1)
    else:
        movie_feat.append(0)
    if movie.Documentary:
        movie_feat.append(1)
    else:
        movie_feat.append(0)

    if movie.War:
        movie_feat.append(1)
    else:
        movie_feat.append(0)
    if movie.Musical:
        movie_feat.append(1)
    else:
        movie_feat.append(0)
    if movie.Western:
        movie_feat.append(1)
    else:
        movie_feat.append(0)
    if movie.Film_Noir:
        movie_feat.append(1)
    else:
        movie_feat.append(0)
    
    response = requests.post('http://api:80/genres/predict', json={'input': movie_feat, 'title': title})
    movies = []
    if response.status_code == 200:
        movies = response.json()['movies']
        
    context = {'similar': movies, 'movie': movie}

    return render(request, 'main/recommendations.html', context)
    

@login_required
def Genres(request):
    if request.method == 'POST':
        movie_feat = []
        movie_genres = []

        if(request.POST.get('Adventure')):
            movie_genres.append('Adventure')
            movie_feat.append(1)
        else:
            movie_feat.append(0)
        if(request.POST.get('Animation')):
            movie_genres.append('Animation')
            movie_feat.append(1)
        else:
            movie_feat.append(0)
        if(request.POST.get('Children')):
            movie_genres.append('Children')
            movie_feat.append(1)
        else:
            movie_feat.append(0)
        if(request.POST.get('Comedy')):
            movie_genres.append('Comedy')
            movie_feat.append(1)
        else:
            movie_feat.append(0)
        if(request.POST.get('Fantasy')):
            movie_genres.append('Fantasy')
            movie_feat.append(1)
        else:
            movie_feat.append(0)
        if(request.POST.get('Romance')):
            movie_genres.append('Romance')
            movie_feat.append(1)
        else:
            movie_feat.append(0)
        if(request.POST.get('Drama')):
            movie_genres.append('Drama')
            movie_feat.append(1)
        else:
            movie_feat.append(0)
        if(request.POST.get('Action')):
            movie_genres.append('Action')
            movie_feat.append(1)
        else:
            movie_feat.append(0)
        if(request.POST.get('Crime')):
            movie_genres.append('Crime')
            movie_feat.append(1)
        else:
            movie_feat.append(0)
        if(request.POST.get('Thriller')):
            movie_genres.append('Thriller')
            movie_feat.append(1)
        else:
            movie_feat.append(0)
        if(request.POST.get('Horror')):
            movie_genres.append('Horror')
            movie_feat.append(1)
        else:
            movie_feat.append(0)
        if(request.POST.get('Mystery')):
            movie_genres.append('Mystery')
            movie_feat.append(1)
        else:
            movie_feat.append(0)
        if(request.POST.get('Sci_Fi')):
            movie_genres.append('Sci_Fi')
            movie_feat.append(1)
        else:
            movie_feat.append(0)
        if(request.POST.get('IMAX')):
            movie_genres.append('IMAX')
            movie_feat.append(1)
        else:
            movie_feat.append(0)
        if(request.POST.get('Documentary')):
            movie_genres.append('Documentary')
            movie_feat.append(1)
        else:
            movie_feat.append(0)
        
        if(request.POST.get('War')):
            movie_genres.append('War')
            movie_feat.append(1)
        else:
            movie_feat.append(0)
        if(request.POST.get('Musical')):
            movie_genres.append('Musical')
            movie_feat.append(1)
        else:
            movie_feat.append(0)
        if(request.POST.get('Western')):
            movie_genres.append('Western')
            movie_feat.append(1)
        else:
            movie_feat.append(0)
        if(request.POST.get('Film_Noir')):
            movie_genres.append('Film_Noir')
            movie_feat.append(1)
        else:
            movie_feat.append(0)

        response = requests.post('http://api:80/genres/predict', json={'input': movie_feat, 'title': ''})
        movies = []
        if response.status_code == 200:
            movies = response.json()['movies']
            
        context = {'movie_genres': movie_genres, 'similar': movies}
        
        return render(request, 'main/recommendations.html', context)
    return render(request, 'main/search_by_genres.html')


def Logout(request):
    logout(request)
    return redirect('main:Home')