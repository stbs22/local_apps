set number
syntax on
colorscheme default
set smartindent
set tabstop=2
set shiftwidth=2
set expandtab
set ignorecase
set showmode
set showmatch

"nnoremap <Up> <Nop>
"nnoremap <Down> <Nop>
"nnoremap <Left> <Nop>
"nnoremap <Right> <Nop>


nnoremap <Backspace> Xi
nnoremap <Enter> O<Down>
nnoremap 0 $
nnoremap <S-Up> 5<Up>
nnoremap <S-Down> 5<Down>

vnoremap <Backspace> d
"vnoremap <Up> <Nop>
"vnoremap <Down> <Nop>
"vnoremap <Left> <Nop>
"vnoremap <Right> <Nop>

" Uncomment the following to have Vim jump to the last position when                                                       
" reopening a file
if has("autocmd")
  au BufReadPost * if line("'\"") > 0 && line("'\"") <= line("$")
    \| exe "normal! g'\"" | endif
endif
