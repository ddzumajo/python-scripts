# -*- coding: utf-8 -*-
"""

This script creates the matrix of covariances, C, and its inverse, H. With H and the mesoscopic and macroscopic profiles, it computes the conjugates variables.

Created on Thu Jul 14 10:32:27 2016

@author: DiegoDZ
"""
import numpy as np
import os
import shutil

##########################################################
# Compute the matrix of covariances, C, and its inverse, H
##########################################################

# Looking one profile output file: Number of zero rows until the first row with at least one element != 0
number_zeros_lower = 16
# Looking one profile output file: Number of zero rows after the last row with at least one element != 0
number_zeros_upper = 17

# Load covariances files
c00 = np.loadtxt('covariance_density')
c01 = np.loadtxt('covariance_densityInternalEnergy')
c02 = np.loadtxt('covariance_densityCenterOfMassUpperWall')
c03 = np.loadtxt('covariance_densityCenterOfMassLowerWall')
c04 = np.loadtxt('covariance_densityMacroInternalEnergyUpperWall')
c05 = np.loadtxt('covariance_densityMacroInternalEnergyLowerWall')
c10 = np.loadtxt('covariance_internalEnergyDensity')
c11 = np.loadtxt('covariance_internalEnergy')
c12 = np.loadtxt('covariance_internalEnergyCenterOfMassUpperWall')
c13 = np.loadtxt('covariance_internalEnergyCenterOfMassLowerWall')
c14 = np.loadtxt('covariance_internalEnergyMacroInternalEnergyUpperWall')
c15 = np.loadtxt('covariance_internalEnergyMacroInternalEnergyLowerWall')
c20 = np.loadtxt('covariance_centerOfMassUpperWallDensity')
c21 = np.loadtxt('covariance_centerOfMassUpperWallInternalEnergy')
c22 = np.loadtxt('covariance_centerOfMassUpperWall')
c23 = np.loadtxt('covariance_centerOfMassUpperLowerWall')
c24 = np.loadtxt('covariance_macroInternalEnergyCenterOfMassUpperWall')
c25 = np.loadtxt('covariance_macroInternalEnergyLowerWallCenterOfMassUpperWall')
c30 = np.loadtxt('covariance_centerOfMassLowerWallDensity')
c31 = np.loadtxt('covariance_centerOfMassLowerWallInternalEnergy')
c32 = np.loadtxt('covariance_centerOfMassUpperLowerWall')
c33 = np.loadtxt('covariance_centerOfMassLowerWall')
c34 = np.loadtxt('covariance_macroInternalEnergyUpperWallCenterOfMassLowerWall')
c35 = np.loadtxt('covariance_macroInternalEnergyCenterOfMassLowerWall')
c40 = np.loadtxt('covariance_macroInternalEnergyUpperWallDensity')
c41 = np.loadtxt('covariance_macroInternalEnergyUpperWallInternalEnergy')
c42 = np.loadtxt('covariance_macroInternalEnergyCenterOfMassUpperWall')
c43 = np.loadtxt('covariance_macroInternalEnergyUpperWallCenterOfMassLowerWall')
c44 = np.loadtxt('covariance_macroInternalEnergyUpperWall')
c45 = np.loadtxt('covariance_macroInternalEnergyUpperLowerWall')
c50 = np.loadtxt('covariance_macroInternalEnergyLowerWallDensity')
c51 = np.loadtxt('covariance_macroInternalEnergyLowerWallInternalEnergy')
c52 = np.loadtxt('covariance_macroInternalEnergyLowerWallCenterOfMassUpperWall')
c53 = np.loadtxt('covariance_macroInternalEnergyCenterOfMassLowerWall')
c54 = np.loadtxt('covariance_macroInternalEnergyUpperLowerWall')
c55 = np.loadtxt('covariance_macroInternalEnergyLowerWall')

# Delete zero elements. In this stage we use number_zeros_lower,number_zeros_upper and number_nodes.
number_nodes = len(c00) # All files have the same number of rows, so it is not necessary to compute the lenght of all files
c00 = c00[number_zeros_lower:number_nodes-number_zeros_upper, number_zeros_lower:number_nodes-number_zeros_upper]
c01 = c01[number_zeros_lower:number_nodes-number_zeros_upper, number_zeros_lower:number_nodes-number_zeros_upper]
c02 = c02[number_zeros_lower:number_nodes-number_zeros_upper]
c03 = c03[number_zeros_lower:number_nodes-number_zeros_upper]
c04 = c04[number_zeros_lower:number_nodes-number_zeros_upper]
c05 = c05[number_zeros_lower:number_nodes-number_zeros_upper]
c10 = c10[number_zeros_lower:number_nodes-number_zeros_upper, number_zeros_lower:number_nodes-number_zeros_upper]
c11 = c11[number_zeros_lower:number_nodes-number_zeros_upper, number_zeros_lower:number_nodes-number_zeros_upper]
c12 = c12[number_zeros_lower:number_nodes-number_zeros_upper]
c13 = c13[number_zeros_lower:number_nodes-number_zeros_upper]
c14 = c14[number_zeros_lower:number_nodes-number_zeros_upper]
c15 = c15[number_zeros_lower:number_nodes-number_zeros_upper]
c20 = c20[number_zeros_lower:number_nodes-number_zeros_upper]
c21 = c21[number_zeros_lower:number_nodes-number_zeros_upper]
c30 = c30[number_zeros_lower:number_nodes-number_zeros_upper]
c31 = c31[number_zeros_lower:number_nodes-number_zeros_upper]
c40 = c40[number_zeros_lower:number_nodes-number_zeros_upper]
c41 = c41[number_zeros_lower:number_nodes-number_zeros_upper]
c50 = c50[number_zeros_lower:number_nodes-number_zeros_upper]
c51 = c51[number_zeros_lower:number_nodes-number_zeros_upper]

# Transform arrays into matrix
C00 = np.asmatrix(c00)
C01 = np.asmatrix(c01)
C02 = np.asmatrix(c02)
C03 = np.asmatrix(c03)
C04 = np.asmatrix(c04)
C05 = np.asmatrix(c05)
C10 = np.asmatrix(c10)
C11 = np.asmatrix(c11)
C12 = np.asmatrix(c12)
C13 = np.asmatrix(c13)
C14 = np.asmatrix(c14)
C15 = np.asmatrix(c15)
C20 = np.asmatrix(c20)
C21 = np.asmatrix(c21)
C22 = np.asmatrix(c22)
C23 = np.asmatrix(c23)
C24 = np.asmatrix(c24)
C25 = np.asmatrix(c25)
C30 = np.asmatrix(c30)
C31 = np.asmatrix(c31)
C32 = np.asmatrix(c32)
C33 = np.asmatrix(c33)
C34 = np.asmatrix(c34)
C35 = np.asmatrix(c35)
C40 = np.asmatrix(c40)
C41 = np.asmatrix(c41)
C42 = np.asmatrix(c42)
C43 = np.asmatrix(c43)
C44 = np.asmatrix(c44)
C45 = np.asmatrix(c45)
C50 = np.asmatrix(c50)
C51 = np.asmatrix(c51)
C52 = np.asmatrix(c52)
C53 = np.asmatrix(c53)
C54 = np.asmatrix(c54)
C55 = np.asmatrix(c55)

# Create the matrix of covariances, C
C = np.bmat([[C00, C01, C02.T, C03.T, C04.T, C05.T],[C10, C11, C12.T, C13.T, C14.T, C15.T],[C20, C21, C22, C23, C24, C25],[C30, C31, C32, C33, C34, C35], [C40, C41, C42, C43, C44, C45], [C50, C51, C52, C53, C54, C55]])

# Compute the inverse of C, H
H = C.I

# Save the matrix H
np.savetxt('H', H)

########################################################################################
# Compute conjugate variables (mu, beta, lambdaUpper, lambdaLower, betaUpper, betaLower)
########################################################################################

# Load profile files.
densityFluid = np.asmatrix(np.loadtxt('mesoDensity_fluid'))
internalEnergyFluid = np.asmatrix(np.loadtxt('mesoInternal_energy_fluid'))
centerOfMassUpperWall = np.asmatrix(np.loadtxt('centerOfMass_UpperWall'))
centerOfMassLowerWall = np.asmatrix(np.loadtxt('centerOfMass_LowerWall'))
macroInternalEnergyUpperWall = np.asmatrix(np.loadtxt('macroInternalEnergy_UpperWall'))
macroInternalEnergyLowerWall = np.asmatrix(np.loadtxt('macroInternalEnergy_LowerWall'))

# Delete zero elements which corresponds to walls nodes.
densityFluid = densityFluid[:,number_zeros_lower:number_nodes-number_zeros_upper]
internalEnergyFluid = internalEnergyFluid[:, number_zeros_lower:number_nodes-number_zeros_upper]

# Introduce new variable called nodes: number of nodes in which the elements are !=0.
nodes = number_nodes - (number_zeros_lower + number_zeros_upper)
# Number snapshots
number_snapshots = len(densityFluid)

# Subtract the last row (system in equilibrium) to all rows: fluctuation of the CG variables.
densityFluid = densityFluid - densityFluid[number_snapshots-1,:]
internalEnergyFluid = internalEnergyFluid - internalEnergyFluid[number_snapshots-1,:]
centerOfMassUpperWall = centerOfMassUpperWall - centerOfMassUpperWall[number_snapshots-1,:]
centerOfMassLowerWall = centerOfMassLowerWall - centerOfMassLowerWall[number_snapshots-1,:]
macroInternalEnergyUpperWall = macroInternalEnergyUpperWall - macroInternalEnergyUpperWall[:,number_snapshots-1]
macroInternalEnergyLowerWall = macroInternalEnergyLowerWall - macroInternalEnergyLowerWall[:,number_snapshots-1]

####
# Compute terms of mu (chemical potential)
####
"""
mu_term_density = np.zeros((number_snapshots,nodes))
mu_term_energy = np.zeros((number_snapshots,nodes))
for t in range(0,number_snapshots):
    for i in range(0,nodes):
        mu_term_density[t,i] = np.sum(H[i,0:nodes] * densityFluid[t,:].T)
        mu_term_energy[t,i] = np.sum(H[i,nodes:2*nodes] * internalEnergyFluid[t,:].T)
mu_term_cmUpper = np.zeros((number_snapshots,nodes))
mu_term_cmLower = np.zeros((number_snapshots,nodes))
mu_term_macroEnergyUpper = np.zeros((number_snapshots,nodes))
mu_term_macroEnergyLower = np.zeros((number_snapshots,nodes))
for i in range(0, nodes):
    mu_term_cmUpper[:,i] = H[i,2*nodes] * centerOfMassUpperWall[:,2].T
    mu_term_cmLower[:,i] = H[i,2*nodes+1] * centerOfMassLowerWall[:,2].T
    mu_term_macroEnergyUpper[:,i] = H[i,2*nodes+2] * macroInternalEnergyUpperWall
    mu_term_macroEnergyLower[:,i] = H[i,2*nodes+3] * macroInternalEnergyLowerWall
# Sum terms
mu = mu_term_density + mu_term_energy + mu_term_cmUpper + mu_term_cmLower + mu_term_macroEnergyUpper + mu_term_macroEnergyLower
"""
####
# Compute terms of beta (temperature)
####
beta_term_density = np.zeros((number_snapshots, nodes))
beta_term_energy = np.zeros((number_snapshots, nodes))
for t in range(0, number_snapshots):
    for i in range(nodes, 2*nodes):
        beta_term_density[t,i-nodes] = np.sum(H[i,0:nodes] * densityFluid[t,:].T)
        beta_term_energy[t,i-nodes] = np.sum(H[i, nodes:2*nodes] * internalEnergyFluid[t,:].T)
beta_term_cmUpper = np.zeros((number_snapshots, nodes))
beta_term_cmLower = np.zeros((number_snapshots, nodes))
beta_term_macroEnergyUpper = np.zeros((number_snapshots, nodes))
beta_term_macroEnergyLower = np.zeros((number_snapshots, nodes))
for i in range(nodes, 2*nodes):
    beta_term_cmUpper[:,i-nodes] = H[i, 2*nodes] * centerOfMassUpperWall[:,2].T
    beta_term_cmLower[:,i-nodes] = H[i, 2*nodes+1] * centerOfMassLowerWall[:,2].T
    beta_term_macroEnergyUpper[:,i-nodes] = H[i, 2*nodes+2] * macroInternalEnergyUpperWall
    beta_term_macroEnergyLower[:,i-nodes] = H[i, 2*nodes+3] * macroInternalEnergyLowerWall
# Sum terms
#beta = beta_term_density + beta_term_energy + beta_term_cmUpper + beta_term_cmLower + beta_term_macroEnergyUpper + beta_term_macroEnergyLower
betaFluid = beta_term_energy + beta_term_macroEnergyUpper + beta_term_macroEnergyLower
betaFluid = np.asmatrix(betaFluid)

####
# Compute terms of lambdaUpper
####
"""
lambdaUpper_term_density = np.zeros(number_snapshots)
lambdaUpper_term_energy = np.zeros(number_snapshots)
for t in range(0, number_snapshots):
     lambdaUpper_term_density[t] = np.sum(H[2*nodes, 0:nodes] * densityFluid[t,:].T)
     lambdaUpper_term_energy[t] = np.sum(H[2*nodes, nodes:2*nodes] * internalEnergyFluid[t,:].T)
lambdaUpper_term_cmUpper = H[2*nodes, 2*nodes] * centerOfMassUpperWall[:,2].T
lambdaUpper_term_cmLower = H[2*nodes, 2*nodes+1] * centerOfMassLowerWall[:,2].T
lambdaUpper_term_macroEnergyUpper = H[2*nodes, 2*nodes+2] * macroInternalEnergyUpperWall
lambdaUpper_term_macroEnergyLower = H[2*nodes, 2*nodes+3] * macroInternalEnergyLowerWall
# Sum terms
lambdaUpper = lambdaUpper_term_density + lambdaUpper_term_energy + lambdaUpper_term_cmUpper + lambdaUpper_term_cmLower + lambdaUpper_term_macroEnergyUpper + lambdaUpper_term_macroEnergyLower
"""
####
# Compute terms of lambdaLower
####
"""
lambdaLower_term_density = np.zeros(number_snapshots)
lambdaLower_term_energy = np.zeros(number_snapshots)
for t in range(0, number_snapshots):
     lambdaLower_term_density[t] = np.sum(H[2*nodes+1, 0:nodes] * densityFluid[t,:].T)
     lambdaLower_term_energy[t] = np.sum(H[2*nodes+1, nodes:2*nodes] * internalEnergyFluid[t,:].T)
lambdaLower_term_cmUpper = H[2*nodes+1, 2*nodes] * centerOfMassUpperWall[:,2].T
lambdaLower_term_cmLower = H[2*nodes+1, 2*nodes+1] * centerOfMassLowerWall[:,2].T
lambdaLower_term_macroEnergyUpper = H[2*nodes+1, 2*nodes+2] * macroInternalEnergyUpperWall
lambdaLower_term_macroEnergyLower = H[2*nodes+1, 2*nodes+3] * macroInternalEnergyLowerWall
# Sum terms
lambdaLower = lambdaLower_term_density + lambdaLower_term_energy + lambdaLower_term_cmUpper + lambdaLower_term_cmLower + lambdaLower_term_macroEnergyUpper + lambdaLower_term_macroEnergyLower
"""
####
# Compute terms of betaUpper
####
betaUpper_term_density = np.zeros(number_snapshots)
betaUpper_term_energy = np.zeros(number_snapshots)
for t in range(0, number_snapshots):
     betaUpper_term_density[t] = np.sum(H[2*nodes+2, 0:nodes] * densityFluid[t,:].T)
     betaUpper_term_energy[t] = np.sum(H[2*nodes+2, nodes:2*nodes] * internalEnergyFluid[t,:].T)
betaUpper_term_cmUpper = H[2*nodes+2, 2*nodes] * centerOfMassUpperWall[:,2].T
betaUpper_term_cmLower = H[2*nodes+2, 2*nodes+1] * centerOfMassLowerWall[:,2].T
betaUpper_term_macroEnergyUpper = H[2*nodes+2, 2*nodes+2] * macroInternalEnergyUpperWall
betaUpper_term_macroEnergyLower = H[2*nodes+2, 2*nodes+3] * macroInternalEnergyLowerWall
# Sum terms
betaUpper = betaUpper_term_density + betaUpper_term_energy + betaUpper_term_cmUpper + betaUpper_term_cmLower + betaUpper_term_macroEnergyUpper + betaUpper_term_macroEnergyLower

####
# Compute terms of betaLower
####
betaLower_term_density = np.zeros(number_snapshots)
betaLower_term_energy = np.zeros(number_snapshots)
for t in range(0, number_snapshots):
     betaLower_term_density[t] = np.sum(H[2*nodes+3, 0:nodes] * densityFluid[t,:].T)
     betaLower_term_energy[t] = np.sum(H[2*nodes+3, nodes:2*nodes] * internalEnergyFluid[t,:].T)
betaLower_term_cmUpper = H[2*nodes+3, 2*nodes] * centerOfMassUpperWall[:,2].T
betaLower_term_cmLower = H[2*nodes+3, 2*nodes+1] * centerOfMassLowerWall[:,2].T
betaLower_term_macroEnergyUpper = H[2*nodes+3, 2*nodes+2] * macroInternalEnergyUpperWall
betaLower_term_macroEnergyLower = H[2*nodes+3, 2*nodes+3] * macroInternalEnergyLowerWall
# Sum terms
betaLower = betaLower_term_density + betaLower_term_energy + betaLower_term_cmUpper + betaLower_term_cmLower + betaLower_term_macroEnergyUpper + betaLower_term_macroEnergyLower

###
# Compute the term beta solid
###
betaSolid = betaUpper_term_energy + betaLower_term_energy + betaUpper_term_macroEnergyUpper + betaUpper_term_macroEnergyLower + betaLower_term_macroEnergyUpper + betaLower_term_macroEnergyLower
betaSolid = np.asmatrix(betaSolid)

###
# Compute the term betaFinal as beta - betaSolid
###
betaFinal = betaFluid - betaSolid.T #revisar. Hay que restar a cada columna de nodo la columna de betaSolid.


# Save terms
"""
np.savetxt('mu_term_density', mu_term_density)
np.savetxt('mu_term_energy', mu_term_energy)
np.savetxt('mu_term_cmUpper', mu_term_cmUpper)
np.savetxt('mu_term_cmLower', mu_term_cmLower)
np.savetxt('mu_term_macroEnergyUpper', mu_term_macroEnergyUpper)
np.savetxt('mu_term_macroEnergyLower', mu_term_macroEnergyLower)
"""
np.savetxt('beta_term_density', beta_term_density)
np.savetxt('beta_term_energy', beta_term_energy)
np.savetxt('beta_term_cmUpper', beta_term_cmUpper)
np.savetxt('beta_term_cmLower', beta_term_cmLower)
np.savetxt('beta_term_macroEnergyUpper', beta_term_macroEnergyUpper)
np.savetxt('beta_term_macroEnergyLower', beta_term_macroEnergyLower)
"""
np.savetxt('lambdaUpper_term_density', lambdaUpper_term_density)
np.savetxt('lambdaUpper_term_energy', lambdaUpper_term_energy)
np.savetxt('lambdaUpper_term_cmUpper', lambdaUpper_term_cmUpper.T)
np.savetxt('lambdaUpper_term_cmLower', lambdaUpper_term_cmLower.T)
np.savetxt('lambdaUpper_term_macroEnergyUpper', lambdaUpper_term_macroEnergyUpper.T)
np.savetxt('lambdaUpper_term_macroEnergyLower', lambdaUpper_term_macroEnergyLower.T)
np.savetxt('lambdaLower_term_density', lambdaLower_term_density)
np.savetxt('lambdaLower_term_energy', lambdaLower_term_energy)
np.savetxt('lambdaLower_term_cmUpper', lambdaLower_term_cmUpper.T)
np.savetxt('lambdaLower_term_cmLower', lambdaLower_term_cmLower.T)
np.savetxt('lambdaLower_term_macroEnergyUpper', lambdaLower_term_macroEnergyUpper.T)
np.savetxt('lambdaLower_term_macroEnergyLower', lambdaLower_term_macroEnergyLower.T)
"""
np.savetxt('betaUpper_term_density', betaUpper_term_density)
np.savetxt('betaUpper_term_energy', betaUpper_term_energy)
np.savetxt('betaUpper_term_cmUpper', betaUpper_term_cmUpper)
np.savetxt('betaUpper_term_cmLower', betaUpper_term_cmLower.T)
np.savetxt('betaUpper_term_macroEnergyUpper', betaUpper_term_macroEnergyUpper)
np.savetxt('betaUpper_term_macroEnergyLower', betaUpper_term_macroEnergyLower)
np.savetxt('betaLower_term_density', betaLower_term_density)
np.savetxt('betaLower_term_energy', betaLower_term_energy)
np.savetxt('betaLower_term_cmUpper', betaLower_term_cmUpper)
np.savetxt('betaLower_term_cmLower', betaLower_term_cmUpper)
np.savetxt('betaLower_term_macroEnergyUpper', betaLower_term_macroEnergyUpper)
np.savetxt('betaLower_term_macroEnergyLower', betaLower_term_macroEnergyLower)

# Save conjugate variables (mu, beta, lambdaUpper, lambdaLower, betaUpper, betaLower)
#np.savetxt('mu', mu)
np.savetxt('betaFluid', betaFluid)
#np.savetxt('lambdaUpper', lambdaUpper)
#np.savetxt('lambdaLower', lambdaLower)
np.savetxt('betaUpper', betaUpper)
np.savetxt('betaLower', betaLower)
np.savetxt('betaSolid', betaSolid)
np.savetxt('betaFinal', betaFinal) #revisar

# Move the outputs to a new folder named "conjugate_variables"
#shutil.rmtree('./conjugate_variables')
conjugate_variables = r'./conjugate_variables'
if not os.path.exists(conjugate_variables):
    os.makedirs(conjugate_variables)
for f in os.listdir('./'):
    if (f.startswith('mu') or f.startswith('beta') or f.startswith('lambda')):
        shutil.move(f, conjugate_variables)

#EOF
