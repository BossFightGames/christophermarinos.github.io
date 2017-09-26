#lang racket

(define nil '())

(define (elemat list n iter)
  (if (= n iter) (car list) (elemat (cdr list) n (+ iter 1))))

(define (sizecol list iter)
  (cond
    ((null? list) iter)
    (else (sizecol (cdr list) (+ iter 1))))
  )

(define (sizerow list iter)
  (cond
    ((null? list) iter)
    (else (sizerow (cdr list) (+ iter 1)))))

(define (mat2x2det mat2x2)
     (- (* (caar mat2x2) (cadadr mat2x2)) (* (cadar mat2x2) (caadr mat2x2))));no longer needed once determinant rolls out

(define (dotprod a b)
  (if (and (null? a) (null? b)) 0 (+(* (car a) (car b)) (dotprod (cdr a) (cdr b)))));this allows an n length dotprod. it may be better to provide a 0 element which in case of addition is 0

(define (xmulrow list matb iter)
  (if (= iter (sizerow (car matb) 0)) nil (cons (dotprod list (extractnthcolumn matb iter)) (xmulrow list matb (+ iter 1)))))

(define (matmul mata matb);being naughty and letting improperly sized matrices self-correct and by self correct i mean crash the program. This is Scheme.
  (if (null? mata) nil (cons (xmulrow (car mata) matb 0) (matmul (cdr mata) matb))))

(define (extractfirstcolumn a)
 (if (null? a) nil (cons (caar a) (extractfirstcolumn (cdr a))))
  );was to test before extractnthcolumn

(define (extractnthcolumn a n);should b jth column
  (if (null? a) nil (cons (elemat (car a) n 0) (extractnthcolumn (cdr a) n)))
  )

(define (extractnthrow a n)
  (xextractnthrow a n 0))

(define (xextractnthrow a n iter);should be ith row for extra linear algebra authenticity also i need to be consistent w my append-x-iter-hiding methods
  (if (null? a) nil (if (= iter n) (car a) (xextractnthrow (cdr a) n (+ iter 1))))
   
  )

(define (makerowident dim oneindice iter)
  (if (= dim iter) nil (if (= oneindice iter) (cons 1 (makerowident dim oneindice (+ iter 1))) (cons 0 (makerowident dim oneindice (+ iter 1)))))
  ) 

(define (makerowrand dim iter)
  (if (= dim iter) nil (cons (random 9) (makerowrand dim (+ iter 1)))));uses a magic number but this is to test things so i guess it is ok

(define (consrows dim iter)
  (if (= dim iter) nil (cons (makerowident dim iter 0) (consrows dim (+ iter 1)))))

(define (randrows dim iter)
  (if (= dim iter) nil (cons (makerowrand dim 0) (randrows dim (+ iter 1)))))

(define (scalerow row scalar)
  (if (pair? row)  (cons (* scalar (car row)) (scalerow (cdr row) scalar)) nil))

(define (makematident dim)
  (consrows dim 0))

(define (makematrand dim);for testing mult, inversion, row operation etc speeds
  (randrows dim 0))

(define (transpose mat)
  (xtranspose mat 0))

(define (xtranspose mata iter)
(if (= (sizerow (car mata) 0) iter ) nil (cons (extractnthcolumn mata iter) (xtranspose mata (+ iter 1)))))

(define (makeswapelem dim swapa swapb);swapa swapb in range of [0,dim] obviously plz
(xmakeswapelem dim swapa swapb 0))

(define (xmakeswapelem dim swapa swapb iter)


(cond ((= dim iter) nil)
    ((= iter swapa)     (cons (makerowident dim swapb 0) (xmakeswapelem dim  swapa swapb (+ iter 1) ))     )
    ((= iter swapb)      (cons (makerowident dim swapa 0) (xmakeswapelem dim swapa swapb (+ iter 1) ))  )
    (else (   cons (makerowident dim iter 0) (xmakeswapelem dim swapa swapb  (+ iter 1) )))
    )
  
  );makes an MxM swap matrice which when multiplied by a MxN matrice will swap the rows designated by swapa and swapb (refer to a linear algebra text as what is going on here is more than I can stick onto the end of a line of code)

;(define (listelemat l n)


;(define (extractelem mat i j)
; (extractnthcolumn (extractnthrow mat i) j))


(define (colswap mat rowa rowb)
  (transpose(matmul (makeswapelem (sizerow (transpose mat) 0) rowa rowb)  (transpose mat))))

(define (rowswap mat rowa rowb)
  (matmul (makeswapelem (sizerow mat 0) rowa rowb) mat))

(define (directcopy mat iter);flexing my car cdr muscle as my lisp recursions are a wee rusty (no pun intended lol)
  (if (pair? mat)  (cons (car mat) (directcopy (cdr mat))) nil)
  )

(define (scalematrow mat row scalar iter)
  ;algorithm: if row = iter (scalerow with scalar) (scalerow with 1)
  (if (pair? mat)
  (if (= iter row) (cons (scalerow (car mat) scalar) (scalematrow (cdr mat) row scalar (+ iter 1)))
      (cons (scalerow (car mat) 1) (scalematrow (cdr mat) row scalar (+ iter 1))));identity element to the rescue
  nil
  )
  )

(define (matelemat mat i j iter)
  (if (= j iter) (elemat (car mat) i 0) (matelemat (cdr mat) i j (+ iter 1)))
  )

(define (addvecs veca vecb)
  (if (pair? veca)  (cons (+ (car veca) (car vecb)) (addvecs (cdr veca) (cdr vecb))) nil)
  )

(define (addrows mat rowa rowb iter);this will work in conjunction with scalerow to allow matrix solutions. order matters: row a adds to row b. we also as it is currently written need rowa to be an ACTUAL ROW not an indice ie call it as (extractnthrow mat 1 0)
  (if (pair? mat)
      (if (= iter rowb) (cons (addvecs (car mat) rowa) (addrows (cdr mat) rowa rowb (+ iter 1)))
          (cons (car mat) (addrows (cdr mat) rowa rowb (+ iter 1))))
      nil
  ))

(define (form-submatrix mat row col iter);given an mxn matrix returns an (- m 1)x(- n 1) matrix split along the given row and column
  (if (pair? mat) (if (= row iter) (form-submatrix (cdr mat) row col (+ iter 1))
     (cons (delfromvec (car mat) col 0) (form-submatrix (cdr mat) row col (+ iter 1)) ))
  nil)
)

(define (delfromvec vec ind iter)
            (if (pair? vec) (if (= ind iter) (delfromvec (cdr vec) ind (+ iter 1))
             (cons (car vec) (delfromvec (cdr vec) ind (+ iter 1)) ))  nil)
            )


(define (xdeterminant mat row coliter additive-identity mult-identity reflector)
  (if (pair? mat);obviously fix
  (+;add?? i had this done correctly before and deleted it
   (xdeterminant (form-submatrix mat 0 0 0) row coliter)
   (if ()
   additive-identity;which is going to be 0 unless you are into some odd stuff)
   )
  ;else
  mat;fix: extract mat value
  )
  )



;(define (determinant mat)
;  (xdeterminant mat 0 0 0 1 1))
  

(define testmat2x2 '((1 2) (3 4)));det is -2
(define testmat3x3 '((1 2 3) (4 5 6) (7 8 9)))
(define testmat4x3 '((1 2 3 4) (5 6 7 8) (9 10 11 12)))
(define testmat2x3 '((1 2) (3 4) (5 6)))
(define testmat3x2 '((1 2 3) (4 5 6)))
(define testmat3x1 '((1 2 3)))
(define testmat1x3 '((1) (2) (3)))
(define testmat4x4flip '((1 0 0 0)(0 0 1 0)(0 1 0 0)(0 0 0 1)))
(define testmat3x3flip '((1 0 0)(0 0 1)(0 1 0)))