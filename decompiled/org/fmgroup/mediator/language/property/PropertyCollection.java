/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.property;

import java.util.HashMap;
import java.util.Map;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.common.UtilCode;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.property.Property;

public class PropertyCollection
implements RawElement {
    private RawElement parent;
    private Map<String, Property> properties = new HashMap<String, Property>();

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public PropertyCollection setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    public PropertyCollection putProperty(String name, Property prop) throws ValidationException {
        prop.setParent(this);
        if (this.properties.containsKey(name)) {
            throw ValidationException.DumplicatedIdentifier(name, "property name");
        }
        this.properties.put(name, prop);
        return this;
    }

    @Override
    public PropertyCollection fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.PropertySegmentContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "PropertySegmentContext", context.toString());
        }
        for (int i = 0; i < ((MediatorLangParser.PropertySegmentContext)context).ID().size(); ++i) {
            this.putProperty(((MediatorLangParser.PropertySegmentContext)context).ID(i).getText(), new Property().setParent(this).fromContext(((MediatorLangParser.PropertySegmentContext)context).property(i), this));
        }
        return this;
    }

    @Override
    public PropertyCollection copy(RawElement parent) throws ValidationException {
        PropertyCollection props = new PropertyCollection();
        props.setParent(parent);
        throw ValidationException.UnderDevelopment();
    }

    public String toString() {
        String props = "";
        for (String name : this.properties.keySet()) {
            props = props + String.format("%s: %s;\n", name, this.properties.get(name).toString());
        }
        return String.format("properties {\n%s}\n", UtilCode.addIndent(props, 1));
    }
}

