===============================================================================
almira.rpm.cmake - change history
===============================================================================

Version 3.7.0-1 (21 November 2016)
----------------------------------
* Updated to version 3.7.0


Version 3.6.1-1
---------------

3.6.1 does not compile!
It requires OpenSSL, and there's something wrong with the setup we have:

lib/libcmcurl.a(openssl.c.o): In function `ossl_connect_step2':
/home/quickbuild/workspace/root/packages/cmake/BUILD/cmake-3.6.1/Utilities/cmcurl/lib/vtls/openssl.c:2219: undefined reference to `SSL_get0_alpn_selected'
lib/libcmcurl.a(openssl.c.o): In function `ossl_connect_step1':
/home/quickbuild/workspace/root/packages/cmake/BUILD/cmake-3.6.1/Utilities/cmcurl/lib/vtls/openssl.c:1918: undefined reference to `SSL_CTX_set_alpn_protos'
collect2: ld returned 1 exit status
make[2]: *** [Utilities/cmcurl/LIBCURL] Error 1
make[1]: *** [Utilities/cmcurl/CMakeFiles/LIBCURL.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
make: *** [all] Error 2

openssl version
OpenSSL 1.0.2h  3 May 2016


Version 3.5.2-1 (15 April 2016)
-------------------------------
* Updated to version 3.5.2


Version 3.5.0-1 (12 March 2016)
-------------------------------
* Updated to version 3.5.0


Version 3.4.2-1 (04 February 2016)
----------------------------------
* Updated to version 3.4.2


Version 3.4.1-1 (05 December 2015)
----------------------------------
* Updated to version 3.4.1


Version 3.4.0-1 (14 November 2015)
----------------------------------
* Updated to version 3.4.0


Version 3.3.2-1 (04 October 2015)
---------------------------------
* Updated to version 3.3.2


Version 3.3.0-1 (25 July 2015)
------------------------------
* Updated to version 3.3.0


Version 3.2.3-1 (04 June 2015)
------------------------------
* Updated to version 3.2.3


Version 3.2.2-1 (20 April 2015)
-------------------------------
* Updated to version 3.2.2


Version 3.2.1-2 (12 March 2015)
-------------------------------
* Updated to version 3.2.1


Version 3.1.3-1 (22 February 2015)
----------------------------------
* Updated to version 3.1.3


Version 3.1.0-1 (23 December 2014)
----------------------------------
* Updated to version 3.1.0


Version 3.0.2-1 (20 September 2014)
-----------------------------------
* Updated to version 3.0.2


Version 3.0.0-1 (14 June 2014)
------------------------------
* Updated to version 3.0.0


Version 2.8.12.2-1 (03 February 2014)
-------------------------------------
* Updated to version 2.8.12.2


Version 2.8.12.1-1 (20 November 2013)
-------------------------------------
* Updated to version 2.8.12.1


Version 2.8.12-1 (19 October 2013)
----------------------------------
* Updated to version 2.8.12


Version 2.8.11.2-1 (09 July 2013)
---------------------------------
* Updated to version 2.8.11.2


Version 2.8.11.1-1 (14 June 2013)
---------------------------------
* Updated to version 2.8.11.1


Version 2.8.11-1 (25 May 2013)
------------------------------
* First Version
