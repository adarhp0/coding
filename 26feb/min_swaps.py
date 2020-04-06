tes=int(input())
for t in range(tes):
    n=int(input())
    s=input()
    st=list(s)
    co=0
    lc=0
    rc=0
    for i in range(n):
        if st[i]=='[':
            lc=lc+1
        else:
            rc=rc+1
        if rc>lc:
            for j in range(i+1,n):
                if st[j]=='[':
                    st[i]='['
                    st[j]=']'
                    lc=lc+1
                    rc=rc-1
                    co=co+1
                    break
    print(co)


    '''
    while(n1>1):
        #print(i,j)
        #print(st)
        a1=st[i]
        a2=st[j]
        if a1=='[' and a2==']':
            st.pop(j)
            st.pop(i)
            if i>0:
                i=i-1
            if j>1:
                j=j-1
            n1=n1-2
        elif a1==']' and a2=='[':
            st.pop(j)
            st.pop(i)
            if i>0:
                i=i-1
            if j>1:
                j=j-1
            n1=n1-2
            co=co+1
        else:
            i=i+1
            j=j+1
    print(co)
    '''
    '''
    while(n1!=n):
        st.append(sl[n1])
        top=top+1
        n1=n1+1
        if st[top-1]=='[' and st[top]==']':
            st.pop()
            st.pop()
            st.append(sl[n1])
            n1=n1+1
            top=top-1
    for i in range(1,n):
        st.append(sl[i])
        top=top+1
        if st[top-1]=='[' and st[top]==']':
            st.pop()
            st.pop()
    '''
        