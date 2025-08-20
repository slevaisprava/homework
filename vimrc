set nocompatible
let g:is_lorc_plugin_loaded = 0
set t_Co=256 
let $TERM='xterm-256color'
language en_US.UTF-8
nnoremap * *N
vnoremap * y :execute ":let @/=@\""<CR> :execute "set hlsearch"<CR>
map <F2> :buffers<cr>:b<Space> 
let mapleader = ','

set enc=utf-8
set fileencodings=utf-8,cp1251,latin1,default,koi8-r,ucs-bom
syntax on

colorscheme rdark
set tgc

command W w !sudo tee % > /dev/null

imap <M-'> ''<Esc>i
imap <M-9> ()<Esc>i
imap <M-[> []<Esc>i
imap <M-p> {}<Esc>i


map <M-o> :noh<cr>
"map <M-o> :browse sp<cr> 

"
"set guifont=DejaVu\ Sans\ Mono\ 9
"set guifont=Ubuntu\ Mono\ 12
set guifont=Monaco:h14
"set guifont=Droid\ Sans\ Mono\ Slashed\ 9

"set wildmenu
"set wildmode=list,full

set history=160
set wildmenu
set cpo-=<
set wcm=<C-Z>

set hlsearch
set nowrap
set go+=c
set go-=m
set go-=T
set go-=r
set go-=R
set go-=L
set go-=l
set go-=b
"set go-=e
set noswapfile
set nowritebackup
set nobackup
set fdm=marker
set wmw=0
set wmh=0

set  sessionoptions=tabpages,sesdir

set fillchars=stl:\ ,vert::,fold:\ 
"set fillchars=stl:\:,vert:o,fold:-
"cd /dev/shm

vmap <C-C> "+y
map <C-V> "+gP	

"====================================================================================================================


au BufNewFile	*.orc  0r ~/.vim/skel/orc.skel | 7   
au BufNewFile	*.lorc  0r ~/.vim/skel/lorc.skel | 17   

"au BufNewFile		*.sco  0r ~/.vim/skel/sco.skel
"command -nargs=1 New exec "vs "."<args>".".sco | sp "."<args>".".orc"  	 
command -nargs=0 Sc exe "set filetype=supercollider"
"autocmd WinNew * wincmd H

set  foldtext=v:folddashes.substitute(getline(v:foldstart),'//\\\|;\\\|\\*/\\\|{{{','','g')

hi Pmenu guibg=white guifg=black
hi PmenuSel gui=bold guibg=LightYellow2 guifg=black


"Язык:
set enc=utf-8
set fileencodings=utf-8
set keymap=russian-jcukenwin
imap <C-F12>  
cmap <C-F12>  
set iminsert=0  
set imsearch=0
highlight lCursor guifg=NONE guibg=Green

"nmap j gj
"nmap k gk

:hi MatchParen guibg=#1e2426 guifg=red
set sidescroll=1
	

let &t_SI = "\<Esc>[5 q"
let &t_SR = "\<Esc>[4 q"
let &t_EI = "\<Esc>[0 q"	

set nofoldenable
set timeout timeoutlen=400 ttimeoutlen=1
map <silent> t :tabnext<cr>
map <silent> <M-t> :bo terminal<cr>
imap <silent> jj <Esc>
set macmeta
nnoremap <ScrollWheelRight> <Nop>
nnoremap <ScrollWheelLeft> <Nop>

set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab
set sts=-1
set autoindent

set statusline=%f%=%l:%L-%c 
set laststatus=2
let g:jedi#force_py_version=312
nmap <D-/> gcc
vmap <D-/> gc
vmap / gc
nmap / gcc
