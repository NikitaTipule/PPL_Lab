
;; Function main (main, funcdef_no=0, decl_uid=1792, cgraph_uid=0, symbol_order=0)

main ()
{
  int c;
  int b;
  int a;
  int D.1798;

  _1 = a + c;
  _2 = b + _1;
  _3 = c + a;
  b = _2 * _3;
  D.1798 = b;
  goto <D.1799>;
  D.1798 = 0;
  goto <D.1799>;
  <D.1799>:
  return D.1798;
}


