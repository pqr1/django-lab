from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from django.db.models import Count
from .models import Book, Student, Address
def search(request): #Lab6 نستقبل طلب من المستخدم request
    return render(request, 'bookmodule/search.html')# render نقول للنظام اعرض صفحة HTML 

def __getBooksList():#Lab6
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble'}
    book2 = {'id':56788765,'title':'Reversing', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'Machine Learning', 'author':'Burkov'}
    return [book1, book2, book3]

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and') #هنا بيطلع لي الكتب الي فيها and
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 10)[:10] #سويت شرط
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks}) # اذا لقى كتاب على الاقل يوديه لصفحة الكتب
    else:
        return render(request, 'bookmodule/index.html') # اذا ما لقى يروح للصفحة الرئيسية



#Lab8////////////////////////////////////////////////////////////////////////////////////////////////////////////


def task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/bookList.html', {'books': books})

def task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) &
        (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/bookList.html', {'books': books})

def task3(request):
    books = Book.objects.filter(
        Q(edition__lte=3) &
        ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/bookList.html', {'books': books})

def task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books': books})

def task5(request):
    data = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'data': data})

def task7(request):
    data = Student.objects.values('address__city').annotate(total=Count('id'))
    return render(request, 'bookmodule/task7.html', {'data': data})



#Lab8///////////////////////////////////////////////////////////////////////////////////////////////////////////




def search(request): #Lab6
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False

            if isTitle and string in item['title'].lower():
                contained = True

            if not contained and isAuthor and string in item['author'].lower():
                contained = True

            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')

def html5_links(request):
    return render(request, 'bookmodule/links.html')

def text_formatting(request):
    return render(request, 'bookmodule/formatting.html')

def listing(request):
    return render(request, 'bookmodule/listing.html')

def tables(request):
    return render(request, 'bookmodule/tables.html')
def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))





