class HtmlPageSerializer < ActiveModel::Serializer
  attributes :id, :dom, :created_at
  has_one :session
end
