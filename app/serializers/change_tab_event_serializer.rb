class ChangeTabEventSerializer < ActiveModel::Serializer
  attributes :id, :url, :created_at
  has_one :session
end
