from ij import IJ
from ij.plugin.frame import RoiManager
from ij.measure import ResultsTable

class ScratchAssayAnalyzer(object):
    
    def __init__(self, image):
        self.measureInPixlUnits = False
        self.inputImage = image

    def getRois(self):
        return self.rois
        
    def setCreateMaskMethod(self, createMaskMethod):
        self.createMaskMethod = createMaskMethod

    def setMeasureInPixelUnits(self):
        self.measureInPixlUnits = True

    def setCloseIterations(self, iterations):
        self.closeIterations = iterations

    def setMinimalArea(self, area):
        self.minimalArea = area
        
    def run(self):
        self.createMaskMethod.run()
        mask = self.createMaskMethod.getMask()
        self.morphologicalCloseOnTissue(mask)
        self.createRoisOfGaps(mask)
        ResultsTable.getResultsTable().reset() 
        RoiManager.getInstance().runCommand("measure")

    def morphologicalCloseOnTissue(self, mask):
        IJ.run(mask, "Options...", "iterations="+str(self.closeIterations)+" count=1 pad black do=Open stack");
        IJ.run(mask, "Options...", "iterations=1 count=1 black do=Nothing");

    def createRoisOfGaps(self, mask):
        roiManager = RoiManager.getRoiManager()
        roiManager.reset()
        IJ.run(mask, "Analyze Particles...", "size="+str(self.minimalArea)+"-Infinity circularity=0.00-1.00 show=Nothing add stack")
        roiManager.runCommand(self.inputImage, "Show All");
        self.rois = list(RoiManager.getInstance().getRoisAsArray())

