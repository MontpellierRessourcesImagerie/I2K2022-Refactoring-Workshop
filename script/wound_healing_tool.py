#@ ImagePlus inputImage
#@ String (choices={"variance", "find edges"}, style="listBox") feature
#@ String (visibility=MESSAGE, value="Parameters for the variance_method", required=false) varianceParameterMessage
#@ Float (label="variance filter radius:", value = 20.0) filterRadius
#@ Integer (label="threshold:", value = 1, min = 1) threshold
#@ String (visibility=MESSAGE, value="morphological close parameters", required=false) closeParameterMessage
#@ Integer (label="radius close:", value = 4, min = 0) closeRadius
#@ Float (label="min area of gap:", value=999999) minimalArea
#@ Boolean (label="ignore spatial calibration", value=False) measureInPixelUnits

from fr.cnrs.mri.scratchAssay.analyzer import ScratchAssayAnalyzer
from fr.cnrs.mri.scratchAssay.masks import CreateMaskFromVariance
from fr.cnrs.mri.scratchAssay.masks import CreateMaskFromFindEdges

def main():
    analyzer = getAnalyzer()
    analyzer.run()

def getAnalyzer():
    analyzer = ScratchAssayAnalyzer(inputImage)
    if measureInPixelUnits:
        analyzer.setMeasureInPixelUnits()
    createMaskMethods = {"variance"   : CreateMaskFromVariance(inputImage, filterRadius, threshold), 
                         "find edges" : CreateMaskFromFindEdges(inputImage)}
    analyzer.setCreateMaskMethod(createMaskMethods[feature])
    analyzer.setCloseIterations(closeRadius)
    analyzer.setMinimalArea(minimalArea)
    return analyzer

main()