
;; Function main (main, funcdef_no=23, decl_uid=2444, cgraph_uid=23, symbol_order=23)

main ()
{
  int b;
  int a;
  int D.2455;

  a = 4;
  goto <D.2449>;
  <D.2448>:
  if (a <= 3) goto <D.2452>; else goto <D.2453>;
  <D.2452>:
  b = b + 2;
  goto <D.2454>;
  <D.2453>:
  b = b * 2;
  <D.2454>:
  a = a + 1;
  <D.2449>:
  if (a <= 99) goto <D.2448>; else goto <D.2450>;
  <D.2450>:
  printf ("%d%d", a, b);
  D.2455 = 0;
  goto <D.2456>;
  <D.2456>:
  return D.2455;
}



;; Function printf (<unset-asm-name>, funcdef_no=15, decl_uid=798, cgraph_uid=15, symbol_order=15)

__attribute__((__artificial__, __gnu_inline__, __always_inline__))
printf (const char * restrict __fmt)
{
  int D.2457;

  D.2457 = __printf_chk (1, __fmt, __builtin_va_arg_pack ());
  goto <D.2458>;
  <D.2458>:
  return D.2457;
}


