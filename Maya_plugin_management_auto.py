import maya.cmds as cmds

#List of plugins based on the tasks
plugins_by_task ={
    "Rigging":[
        'matrixNodes' , 'poseInterpolator' , 'cMuscle' , 'Retargeter' , 'ik2Bsolver' ,
        'ikSpringSolver', 'deformerEvaluator', 'tangentConstraint', 'fbxmaya' 
    ],
    "Animation":[
        'fbxmaya', 'poseInterpolator', 'TimeEditor', 'atomImportExport', 'Retargeter',
        'motionCaptureDevice' , 'GameFbxExporter' , 'ik2Bsolver', 'ikSpringSolver',
        'tangentConstraint', 'AbcExport' , 'AbcImport'
    ],
    "Modeling":[
        'invertShape', 'polyRetopo'
    ],
    "VFX":[
        'nCloth', 'nParticle', 'nRigids', 'nHair', 'nCache', 'nConstraint'
    ],
    "Rendering":[
        'arnold', 'mtoa', 'RenderSetup', 'xgenToolkit', 'Turtle', 'Redshift'
    ],

}