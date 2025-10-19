/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.generated;

import org.antlr.v4.runtime.tree.ParseTreeListener;
import org.fmgroup.mediator.language.generated.MediatorLangParser;

public interface MediatorLangListener
extends ParseTreeListener {
    public void enterProg(MediatorLangParser.ProgContext var1);

    public void exitProg(MediatorLangParser.ProgContext var1);

    public void enterDependency(MediatorLangParser.DependencyContext var1);

    public void exitDependency(MediatorLangParser.DependencyContext var1);

    public void enterTypedef(MediatorLangParser.TypedefContext var1);

    public void exitTypedef(MediatorLangParser.TypedefContext var1);

    public void enterPortIdentifier(MediatorLangParser.PortIdentifierContext var1);

    public void exitPortIdentifier(MediatorLangParser.PortIdentifierContext var1);

    public void enterAssignmentStatement(MediatorLangParser.AssignmentStatementContext var1);

    public void exitAssignmentStatement(MediatorLangParser.AssignmentStatementContext var1);

    public void enterSynchronizingStatement(MediatorLangParser.SynchronizingStatementContext var1);

    public void exitSynchronizingStatement(MediatorLangParser.SynchronizingStatementContext var1);

    public void enterReturnStatement(MediatorLangParser.ReturnStatementContext var1);

    public void exitReturnStatement(MediatorLangParser.ReturnStatementContext var1);

    public void enterIteStatement(MediatorLangParser.IteStatementContext var1);

    public void exitIteStatement(MediatorLangParser.IteStatementContext var1);

    public void enterAssertStatement(MediatorLangParser.AssertStatementContext var1);

    public void exitAssertStatement(MediatorLangParser.AssertStatementContext var1);

    public void enterStatements(MediatorLangParser.StatementsContext var1);

    public void exitStatements(MediatorLangParser.StatementsContext var1);

    public void enterTemplate(MediatorLangParser.TemplateContext var1);

    public void exitTemplate(MediatorLangParser.TemplateContext var1);

    public void enterFunction(MediatorLangParser.FunctionContext var1);

    public void exitFunction(MediatorLangParser.FunctionContext var1);

    public void enterLocalVariableDef(MediatorLangParser.LocalVariableDefContext var1);

    public void exitLocalVariableDef(MediatorLangParser.LocalVariableDefContext var1);

    public void enterFunctionInterface(MediatorLangParser.FunctionInterfaceContext var1);

    public void exitFunctionInterface(MediatorLangParser.FunctionInterfaceContext var1);

    public void enterPortsDecl(MediatorLangParser.PortsDeclContext var1);

    public void exitPortsDecl(MediatorLangParser.PortsDeclContext var1);

    public void enterEntityInterface(MediatorLangParser.EntityInterfaceContext var1);

    public void exitEntityInterface(MediatorLangParser.EntityInterfaceContext var1);

    public void enterVariableSegment(MediatorLangParser.VariableSegmentContext var1);

    public void exitVariableSegment(MediatorLangParser.VariableSegmentContext var1);

    public void enterTransitionSegment(MediatorLangParser.TransitionSegmentContext var1);

    public void exitTransitionSegment(MediatorLangParser.TransitionSegmentContext var1);

    public void enterTransitionSingle(MediatorLangParser.TransitionSingleContext var1);

    public void exitTransitionSingle(MediatorLangParser.TransitionSingleContext var1);

    public void enterTransitionGroup(MediatorLangParser.TransitionGroupContext var1);

    public void exitTransitionGroup(MediatorLangParser.TransitionGroupContext var1);

    public void enterPropertySegment(MediatorLangParser.PropertySegmentContext var1);

    public void exitPropertySegment(MediatorLangParser.PropertySegmentContext var1);

    public void enterProperty(MediatorLangParser.PropertyContext var1);

    public void exitProperty(MediatorLangParser.PropertyContext var1);

    public void enterAutomaton(MediatorLangParser.AutomatonContext var1);

    public void exitAutomaton(MediatorLangParser.AutomatonContext var1);

    public void enterComponentSegment(MediatorLangParser.ComponentSegmentContext var1);

    public void exitComponentSegment(MediatorLangParser.ComponentSegmentContext var1);

    public void enterInternalSegment(MediatorLangParser.InternalSegmentContext var1);

    public void exitInternalSegment(MediatorLangParser.InternalSegmentContext var1);

    public void enterConnectionSegment(MediatorLangParser.ConnectionSegmentContext var1);

    public void exitConnectionSegment(MediatorLangParser.ConnectionSegmentContext var1);

    public void enterComponentDecl(MediatorLangParser.ComponentDeclContext var1);

    public void exitComponentDecl(MediatorLangParser.ComponentDeclContext var1);

    public void enterCustomConnection(MediatorLangParser.CustomConnectionContext var1);

    public void exitCustomConnection(MediatorLangParser.CustomConnectionContext var1);

    public void enterBasicConnection(MediatorLangParser.BasicConnectionContext var1);

    public void exitBasicConnection(MediatorLangParser.BasicConnectionContext var1);

    public void enterPortCollection(MediatorLangParser.PortCollectionContext var1);

    public void exitPortCollection(MediatorLangParser.PortCollectionContext var1);

    public void enterConnectionOptions(MediatorLangParser.ConnectionOptionsContext var1);

    public void exitConnectionOptions(MediatorLangParser.ConnectionOptionsContext var1);

    public void enterConnectionOption(MediatorLangParser.ConnectionOptionContext var1);

    public void exitConnectionOption(MediatorLangParser.ConnectionOptionContext var1);

    public void enterConnectionOptionItem(MediatorLangParser.ConnectionOptionItemContext var1);

    public void exitConnectionOptionItem(MediatorLangParser.ConnectionOptionItemContext var1);

    public void enterSystem(MediatorLangParser.SystemContext var1);

    public void exitSystem(MediatorLangParser.SystemContext var1);

    public void enterMeta(MediatorLangParser.MetaContext var1);

    public void exitMeta(MediatorLangParser.MetaContext var1);

    public void enterNotPathFormulae(MediatorLangParser.NotPathFormulaeContext var1);

    public void exitNotPathFormulae(MediatorLangParser.NotPathFormulaeContext var1);

    public void enterExistsPathFormulae(MediatorLangParser.ExistsPathFormulaeContext var1);

    public void exitExistsPathFormulae(MediatorLangParser.ExistsPathFormulaeContext var1);

    public void enterBracketPathFormulae(MediatorLangParser.BracketPathFormulaeContext var1);

    public void exitBracketPathFormulae(MediatorLangParser.BracketPathFormulaeContext var1);

    public void enterAllPathFormulae(MediatorLangParser.AllPathFormulaeContext var1);

    public void exitAllPathFormulae(MediatorLangParser.AllPathFormulaeContext var1);

    public void enterBinaryPathFormulae(MediatorLangParser.BinaryPathFormulaeContext var1);

    public void exitBinaryPathFormulae(MediatorLangParser.BinaryPathFormulaeContext var1);

    public void enterAtomicPathFormulae(MediatorLangParser.AtomicPathFormulaeContext var1);

    public void exitAtomicPathFormulae(MediatorLangParser.AtomicPathFormulaeContext var1);

    public void enterNotStateFormulae(MediatorLangParser.NotStateFormulaeContext var1);

    public void exitNotStateFormulae(MediatorLangParser.NotStateFormulaeContext var1);

    public void enterPathStateFormulae(MediatorLangParser.PathStateFormulaeContext var1);

    public void exitPathStateFormulae(MediatorLangParser.PathStateFormulaeContext var1);

    public void enterGloballyStateFormulae(MediatorLangParser.GloballyStateFormulaeContext var1);

    public void exitGloballyStateFormulae(MediatorLangParser.GloballyStateFormulaeContext var1);

    public void enterBinaryStateFormulae(MediatorLangParser.BinaryStateFormulaeContext var1);

    public void exitBinaryStateFormulae(MediatorLangParser.BinaryStateFormulaeContext var1);

    public void enterBracketStateFormulae(MediatorLangParser.BracketStateFormulaeContext var1);

    public void exitBracketStateFormulae(MediatorLangParser.BracketStateFormulaeContext var1);

    public void enterFinallyStateFormulae(MediatorLangParser.FinallyStateFormulaeContext var1);

    public void exitFinallyStateFormulae(MediatorLangParser.FinallyStateFormulaeContext var1);

    public void enterNextStateFormulae(MediatorLangParser.NextStateFormulaeContext var1);

    public void exitNextStateFormulae(MediatorLangParser.NextStateFormulaeContext var1);

    public void enterUntilStateFormulae(MediatorLangParser.UntilStateFormulaeContext var1);

    public void exitUntilStateFormulae(MediatorLangParser.UntilStateFormulaeContext var1);

    public void enterTerms(MediatorLangParser.TermsContext var1);

    public void exitTerms(MediatorLangParser.TermsContext var1);

    public void enterValueTerm(MediatorLangParser.ValueTermContext var1);

    public void exitValueTerm(MediatorLangParser.ValueTermContext var1);

    public void enterIteTerm(MediatorLangParser.IteTermContext var1);

    public void exitIteTerm(MediatorLangParser.IteTermContext var1);

    public void enterBinaryOprTerm(MediatorLangParser.BinaryOprTermContext var1);

    public void exitBinaryOprTerm(MediatorLangParser.BinaryOprTermContext var1);

    public void enterElementTerm(MediatorLangParser.ElementTermContext var1);

    public void exitElementTerm(MediatorLangParser.ElementTermContext var1);

    public void enterBracketTerm(MediatorLangParser.BracketTermContext var1);

    public void exitBracketTerm(MediatorLangParser.BracketTermContext var1);

    public void enterStructTerm(MediatorLangParser.StructTermContext var1);

    public void exitStructTerm(MediatorLangParser.StructTermContext var1);

    public void enterTupleTerm(MediatorLangParser.TupleTermContext var1);

    public void exitTupleTerm(MediatorLangParser.TupleTermContext var1);

    public void enterSingleOprTerm(MediatorLangParser.SingleOprTermContext var1);

    public void exitSingleOprTerm(MediatorLangParser.SingleOprTermContext var1);

    public void enterListTerm(MediatorLangParser.ListTermContext var1);

    public void exitListTerm(MediatorLangParser.ListTermContext var1);

    public void enterCallTerm(MediatorLangParser.CallTermContext var1);

    public void exitCallTerm(MediatorLangParser.CallTermContext var1);

    public void enterFieldTerm(MediatorLangParser.FieldTermContext var1);

    public void exitFieldTerm(MediatorLangParser.FieldTermContext var1);

    public void enterIntValue(MediatorLangParser.IntValueContext var1);

    public void exitIntValue(MediatorLangParser.IntValueContext var1);

    public void enterDoubleValue(MediatorLangParser.DoubleValueContext var1);

    public void exitDoubleValue(MediatorLangParser.DoubleValueContext var1);

    public void enterStrValue(MediatorLangParser.StrValueContext var1);

    public void exitStrValue(MediatorLangParser.StrValueContext var1);

    public void enterBoolValue(MediatorLangParser.BoolValueContext var1);

    public void exitBoolValue(MediatorLangParser.BoolValueContext var1);

    public void enterPortVarValue(MediatorLangParser.PortVarValueContext var1);

    public void exitPortVarValue(MediatorLangParser.PortVarValueContext var1);

    public void enterIdValue(MediatorLangParser.IdValueContext var1);

    public void exitIdValue(MediatorLangParser.IdValueContext var1);

    public void enterNullValue(MediatorLangParser.NullValueContext var1);

    public void exitNullValue(MediatorLangParser.NullValueContext var1);

    public void enterBracketType(MediatorLangParser.BracketTypeContext var1);

    public void exitBracketType(MediatorLangParser.BracketTypeContext var1);

    public void enterCharType(MediatorLangParser.CharTypeContext var1);

    public void exitCharType(MediatorLangParser.CharTypeContext var1);

    public void enterDoubleType(MediatorLangParser.DoubleTypeContext var1);

    public void exitDoubleType(MediatorLangParser.DoubleTypeContext var1);

    public void enterTemplateType(MediatorLangParser.TemplateTypeContext var1);

    public void exitTemplateType(MediatorLangParser.TemplateTypeContext var1);

    public void enterIdType(MediatorLangParser.IdTypeContext var1);

    public void exitIdType(MediatorLangParser.IdTypeContext var1);

    public void enterAbstractType(MediatorLangParser.AbstractTypeContext var1);

    public void exitAbstractType(MediatorLangParser.AbstractTypeContext var1);

    public void enterIntType(MediatorLangParser.IntTypeContext var1);

    public void exitIntType(MediatorLangParser.IntTypeContext var1);

    public void enterEnumType(MediatorLangParser.EnumTypeContext var1);

    public void exitEnumType(MediatorLangParser.EnumTypeContext var1);

    public void enterTupleType(MediatorLangParser.TupleTypeContext var1);

    public void exitTupleType(MediatorLangParser.TupleTypeContext var1);

    public void enterInitType(MediatorLangParser.InitTypeContext var1);

    public void exitInitType(MediatorLangParser.InitTypeContext var1);

    public void enterListType(MediatorLangParser.ListTypeContext var1);

    public void exitListType(MediatorLangParser.ListTypeContext var1);

    public void enterBoolType(MediatorLangParser.BoolTypeContext var1);

    public void exitBoolType(MediatorLangParser.BoolTypeContext var1);

    public void enterBoundedIntType(MediatorLangParser.BoundedIntTypeContext var1);

    public void exitBoundedIntType(MediatorLangParser.BoundedIntTypeContext var1);

    public void enterStructType(MediatorLangParser.StructTypeContext var1);

    public void exitStructType(MediatorLangParser.StructTypeContext var1);

    public void enterNullType(MediatorLangParser.NullTypeContext var1);

    public void exitNullType(MediatorLangParser.NullTypeContext var1);

    public void enterUnionType(MediatorLangParser.UnionTypeContext var1);

    public void exitUnionType(MediatorLangParser.UnionTypeContext var1);

    public void enterTypeorvalue(MediatorLangParser.TypeorvalueContext var1);

    public void exitTypeorvalue(MediatorLangParser.TypeorvalueContext var1);

    public void enterScopedID(MediatorLangParser.ScopedIDContext var1);

    public void exitScopedID(MediatorLangParser.ScopedIDContext var1);
}

