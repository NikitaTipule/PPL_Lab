
;; Function main (main, funcdef_no=0, decl_uid=1793, cgraph_uid=0, symbol_order=1)

main ()
{
  int a;
  int i;
  int D.1801;

  a = 10;
  i = 0;
  goto <D.1798>;
  <D.1797>:
  N.0_1 = N;
  a = a + N.0_1;
  i = i + 1;
  <D.1798>:
  if (i <= 3) goto <D.1797>; else goto <D.1799>;
  <D.1799>:
  D.1801 = a;
  goto <D.1802>;
  D.1801 = 0;
  goto <D.1802>;
  <D.1802>:
  return D.1801;
}


