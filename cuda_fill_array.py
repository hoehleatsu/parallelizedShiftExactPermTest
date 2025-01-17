from numba import cuda
@cuda.jit("(u4[:,:,:],u4[:,:,:], u2, u2[:,:],u2[:])")
def fill_array_u4_v_u2(X1,X2, i_, z_,S):
    n = X1.shape[0]
    m = X1.shape[1]
    L = X1.shape[2]

    s, j, z = cuda.grid(3)
    
    if j >= m + 1 or s > S[z] or z >= L:
        return

    if i_ < j:
        X2[s, j - 1, z] = 0
    
    elif j==1 and  s == z_[z, i_ - 1]:
        X2[s, j - 1, z] = X1[s, j - 1, z] + 1
    
    elif j==1 and  s != z_[z, i_ - 1]:
        X2[s, j - 1, z] = X1[s, j - 1, z]
    
    elif j>1 and z_[z, i_ - 1] <= s:
        X2[s, j - 1, z] = X1[s - int(z_[z, i_ - 1]), j - 2, z] + X1[s, j - 1, z]
    
    elif j>1 and z_[z, i_ - 1] > s:
        X2[s, j-1, z] = X1[s,j-1, z]



@cuda.jit("(f8[:,:,:],f8[:,:,:], u2, u2[:,:],u2[:])")
def fill_array_f8_v_u2(X1,X2, i_, z_,S):
    n = X1.shape[0]
    m = X1.shape[1]
    L = X1.shape[2]

    s, j, z = cuda.grid(3)
    
    if j >= m + 1 or s > S[z] or z >= L:
        return

    if i_ < j:
        X2[s, j - 1, z] = 0
    
    elif j==1 and  s == z_[z, i_ - 1]:
        X2[s, j - 1, z] = X1[s, j - 1, z] + 1
    
    elif j==1 and  s != z_[z, i_ - 1]:
        X2[s, j - 1, z] = X1[s, j - 1, z]
    
    elif j>1 and z_[z, i_ - 1] <= s:
        X2[s, j - 1, z] = X1[s - int(z_[z, i_ - 1]), j - 2, z] + X1[s, j - 1, z]
    
    elif j>1 and z_[z, i_ - 1] > s:
        X2[s, j-1, z] = X1[s,j-1, z]

@cuda.jit("(f8[:,:,:],f8[:,:,:], u4, u4[:,:],u4[:])")
def fill_array_f8_v_u4(X1,X2, i_, z_,S):
    n = X1.shape[0]
    m = X1.shape[1]
    L = X1.shape[2]

    s, j, z = cuda.grid(3)
    
    if j >= m + 1 or s > S[z] or z >= L:
        return

    if i_ < j:
        X2[s, j - 1, z] = 0
    
    elif j==1 and  s == z_[z, i_ - 1]:
        X2[s, j - 1, z] = X1[s, j - 1, z] + 1
    
    elif j==1 and  s != z_[z, i_ - 1]:
        X2[s, j - 1, z] = X1[s, j - 1, z]
    
    elif j>1 and z_[z, i_ - 1] <= s:
        X2[s, j - 1, z] = X1[s - int(z_[z, i_ - 1]), j - 2, z] + X1[s, j - 1, z]
    
    elif j>1 and z_[z, i_ - 1] > s:
        X2[s, j-1, z] = X1[s,j-1, z]
