from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm

# List all notes
def note_list(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'note_list.html', {'notes': notes})

# Create a new note
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'note_create.html', {'form': form})

# View note details
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'note_detail.html', {'note': note})

# Delete a note
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'note_delete.html', {'note': note})
