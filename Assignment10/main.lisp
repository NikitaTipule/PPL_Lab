(defun nth (n list)
  "Returns the Nth element of LIST.
N counts from zero.  If LIST is not that long, nil is returned."
  (car (nthcdr n list)))



"Break 9 [10]> (nth 4 '(a b c d))
NIL"
