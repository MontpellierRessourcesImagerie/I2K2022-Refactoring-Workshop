from ij import IJ

class CreateMask(object):

    def __init__(self, image):
        self.inputImage = image
        self.mask = image.duplicate()

    def run(self):
        self.calculateFeature()
        self.setThresholds()
        self.convertToMask()

    def calculateFeature(self):
        pass

    def setThresholds(self):
        pass

    def convertToMask(self):
        IJ.run(self.mask, "Convert to Mask", " black");

    def getMask(self):
        return self.mask
    
class CreateMaskFromVariance(CreateMask):

    def __init__(self, image, radius, threshold):
        CreateMask.__init__(self, image)
        self.radius = radius
        self.threshold = threshold

    def calculateFeature(self):
        IJ.run(self.mask, "Variance...", "radius=" + str(self.radius) + " stack");
        IJ.run(self.mask, "8-bit", "");

    def setThresholds(self):
        IJ.setThreshold(self.mask, 0, self.threshold);   
    
class CreateMaskFromFindEdges(CreateMask):

    def __init__(self, image):
        CreateMask.__init__(self, image)

    def calculateFeature(self):
        IJ.run(self.mask, "Find Edges", "stack");
        IJ.run(self.mask, "Invert", "stack");
        if self.mask.bitDepth==24:
            IJ.run(self.mask, "8-bit", "");

    def setThresholds(self):
        IJ.setAutoThreshold(self.mask, "Percentile dark");
